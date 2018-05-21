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

Singularity hub is where we keep our publicly available images for all to access.
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
