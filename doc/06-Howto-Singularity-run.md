# How to run Singularity containers

## Virtualization vs. Containerization

In our group we make extensive use of virtual machines (VMs).
We utilize VMs that run on our dedicated hardware on UITS managed servers, and we utilize VMs that run on NSF funded Jetstream servers.
Furthermore, we always have the option to buy compute time on VMs hosted on cloud services such as AWS or Google Cloud.
Our use of bgRAMOSE as described in the [Jetstream howto](05-Howto-Jetstream.md) is an excellent representation of how we utilize these.

As wonderful as these VMs are, they also incur significant overhead.
Each VM involves a computer simulating another computer, and an operating system running within another.
As efficiently as this may be implemented, there is just no way around the overhead.
Furthermore, while it is generally straightforward to share/spin up/spin down these machines, it is not necessarily trivial.
Sharing a VM image requires several gigabytes of bandwidth and storage, and once the VM is spun up, the resources that are allocated to it cannot be shared by other processes.

Containerization provides a lightweight alternative to virtualization with many of the benefits and negligible overhead.  
Containerized applications run in isolated environments within the host operating system.
Since they do not run an entire operating system, containers are trivial to spin up and they share resources with other processes running on the same machine.
Furthermore, they are much smaller in size, therefore much easier to distribute.
Finally, it is noteworthy that containers can also run on VMs.

In summary, containers provide portability and reproducibility without significant overhead while VMs can provide compute infrastructure, but with significant overhead.  
When we want to distribute our workflows to predictably run on arbitrary compute platforms, containers are more suitable than virtual machines.

## Singularity

While the industry standard containerization solution is [Docker](0?-Howto-Docker.md), it is not suitable for scientific applications due to various technical reasons.
We therefore use [Singularity](http://singularity.lbl.gov/) as our containerization solution.
Singularity is compatible with Docker images and provides a more suitable feature set for scientific applications.
It is already installed in many academic clusters, and is straightforward to install in any other platform, as the website provides [concise instructions](http://singularity.lbl.gov/install-linux).

Unlike Docker, Singularity does not require any special privileges (sudo etc.) and does not depend on a system-wide daemon running on the background.
In short, if you found that Singularity is installed on your system or you were able to install it locally, you are good to run Singularity containers.

## Recipes, Images, and Instances

**Recipes** are plaintext files that specify a compute environment; this includes the base operating system, commands to install all the necessary programs along with their dependencies, and environment variables.
When we are developing workflows with Singlularity containers, we meticulously prepare recipes (such as [this one](https://github.com/littleblackfish/BWASP/blob/devel/Singularity)) that describe how to build the environment our workflow expects to run in.

**Images** are binary files built from recipes.
Given a recipe, any version of singularity on any machine should build the identical image.
An image can be read-only or writable depending on the use case.
Furthermore, it is possible to modify an image to make another (possibly read-only) image, although this is considered bad form since this modified image cannot be reproduced from a recipe.
One caveat to building images from recipes is that you need sudo privilieges to properly build an image from a recipe.

**Instances** are then images in action.
Every time we run a program within a container, we run another instance of that image.
Unlike VMs, container instances can be spawned, killed and share resources just like any other process.
When we execute a program within a container, we are simply executing that program with a sandbox around it that provides a familiar environment; each such sandbox is an instance of the same image.
It is important to note that these instances do not communicate by default, e.g. a file written by an instance will not be accessible by another unless they are writing to a shared filesystem.

Since building images from recipes takes a bit of time and requires sudo privileges, we prefer to share pre-built images along with our recipes.
This way, those who would like to use our containers can simply download the turn-key solution.

## Singularity Hub

Singularity Hub is where we keep our publicly available images for all to access.
Those brendelgroup projects that are hosted on GitHub and contain Singularity recipes are connected to Singularity Hub.
Singularity images for these projects are automatically built by the Singularity Hub infrastructure every time we push into the GitHub repository.
Singularity offers a convenient way to download these images.
For example :

```
singularity pull --name bwasp.simg shub://brendelgroup/BWASP
```

would download the latest BWASP container image and name it `bwasp.simg`.
This would be the only thing you need to do to run the BWASP workflow, which in fact depends on a number of other programs to function.

## Running Singularity containers

Once you have a working Singularity installation and downloaded a container image (from Singularity Hub or otherwise), you are ready to run.
Singularity comes with a number of subcommands such as `build`, `pull`, `run`, `shell`, but the one you will be utilizing to get work done is mostly `exec`.
The command :

```
singularity exec container.simg command
```

Will execute `command` from within the specified container image.
Let us work through come of the caveats before we move into the additional parameters that we will set.

### Caveat regarding executable paths  

You may or may not have the same `command` executable in your path in the host environment.
For example, let us assume I have genome tools 1.5.7 on my machine (host) but the BWASP container image comes with 1.5.9.
When I am running genometools from within the container, I am running the 1.5.9 version.
This can be easily confirmed by doing :

```
gt --version
singularity exec bwasp.simg gt --version
```

and comparing the outputs.
First one will report the version that is available on the host (or lack of it), and the second one will report the version available in the container.
First one will change depending on where you run it, but the second one will always be the same.
This nicely showcases how convenient (and also disorienting) containers can be.
When we run, for example, `make` within the BWASP container, it uses all the programs as they exist within the container, which may or may not be resemble the environment we have on the host machine.
In fact, we often test our containers on clean installs of various linux distributions where none of the relevant tools other than Singularity is installed.

Had we run the same makefile using the `make` on the host, we would likely get an error due to a missing dependency or different results due to varying versions.
When we use the container we get exactly the same results every time, regardless of the host system, and this is what we mean by **portable** and **reproducible**.

### Caveat regarding the data path

Our programs and workflows operate on data, and we always need to specify where this data is.
Let us say we want to confert a bam file to a sam file using the tools available in the BWASP container.
We can do :

```
singularity exec bwasp.simg samtools view -h file.bam -o file.sam
```

When we provide such relative paths, we are implicitly referring to the working directory.
But where is this working directory in the host, and does it even exist in the container?
This can get tricky.

In practice, this would actually work automagically as long as your working directory is within your home directory as singularity binds your home directory to the same path in the container by default.
However, we often work outside our home directories, in scratch spaces or network mounts where more space is available.
In that case we simply need to specify the folder where the data is, so the container instance has access to it.
If `file.bam` was in a scratch space that is outside our home (`/scratch`), the command would look like this :

```
singularity exec --bind /scratch bwasp.simg samtools view -h /scratch/file.bam  -o /scratch/file.sam
```

And we are good to go, all we needed to add was really `--bind /scratch`.
We also converted to full paths, but this may or may not be necessary depending on the exact set up.
When in doubt, use full paths.

### Recommended parameters

While working with Singularity containers, we found that avoiding some of the automagical features and explicitly specifying these 3 parameters help us avoid surprises.

  1. `--cleanenv` or `-e` : do not inherit environment variables from the host filesystem
  2. `--contain` or `-c` : do not autobind home directory
  3. `--bind path` or `-b path` :  bind this specific path

By using these 3 parameters, we make sure that :  

  1. Custom Python/R/etc. environments that might exist in the host system do not interfere with our container.
  2. The container **does not have access** to any directories that we did not explicitly specify.
  3. The container **does have access** to the path where we have the relevant data, and will have the relevant output written to.

A typical brendelgroup Singluarity command will then look like :

```
singularity exec -e -c -b /scratch/BWASP/data /scratch/BWASP/bwasp.simg make -n
```

which would run `make` from within the container found in `/scratch/BWASP/bwasp.simg` to process the data that is found under `/scratch/BWASP/data`.
This way make uses executables available in the container and all the data I/O is contained to `/scratch/BWASP/data`.
