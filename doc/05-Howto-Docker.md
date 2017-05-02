# Docker applications

[Docker](https://www.docker.com/) is a platform for packaging and running apps in a platform-independent way.
Unlike other virtual machines which can run many applications and even function as complete desktop operating systems, Docker containers are designed to run a single service.

## Running Docker images

The [Docker software](https://www.docker.com/products/overview) must be installed on the computer that is going to run a Docker application.
This is especially easy on Linux, where it can be done at the command line.
Once Docker is installed, it has to be run with sudo privileges.
To use Docker, the Docker daemon must be started with `sudo systemctl start docker`.
Locally available Docker images can be seen with the command `sudo docker images`.
They can be run with `sudo docker run <docker image name>:<optional tag> <arguments>`.
Publicly available Docker images from the [Dockerhub](https://hub.docker.com/) repository can be identified with <repository name>/<docker image>:<optional tag>.
If input or output files from/to the local machine are desired, the volume flag "-v" needs to be used, with the local path on the left side of a colon and the path to which it will be mounted on the right:

```sudo docker run -v /local/path/to/directory:/directory/inside/docker/container <docker image> <arguments>```


```sudo docker run -v $(pwd):/stuff twmccart/discovar-docker:latest READS=/stuff/sample-reads.bam OUT_DIR=/stuff/discovardenovo-assembly-aligned REFHEAD=/stuff/sample-genome```



## Building Docker images

The key to packaging your own application as a Docker image is a script called a Dockerfile.
This script, by default *named* "Dockerfile", is saved in a directory containing any files that the image you are building will need.
Everything in this directory will be imported by the Docker daemon during the build, so don't include extraneous material.
Detailed documentation on creating Dockerfiles is [available](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/) on the Docker website.

Essentially, the Dockerfile is a recipe that takes the form of a series of instructions.
The first instruction is always "FROM", and it designates a base image from which your image will be built.
This will often be one of the Linux images available in the repositories.
Subsequent instructions install software, add files, and set environmental variables and settings.
Each instruction causes the production of a new "layer", which is saved and can be used as a cache if you change a later instruction and rebuild.
A heavily commented example Dockerfile that explains several of the instruction types is available in the [src/](https://github.com/BrendelGroup/bghandbook/tree/master/src) directory.

Once a Dockerfile has been written, the Docker image is built with the `docker build` command.
The "-f" flag designates the name of the Dockerfile if it is something other than "Dockerfile".
The "-t" flag designates a name and optionally a tag for the Docker image in the "name:tag" format.
The only argument `docker build` takes is the path to the directory containing the Dockerfile.
Example:
```
sudo docker build -t discovar-docker:latest -f discovarDockerfile .
```

## Docker Hub

[Docker Hub](https://hub.docker.com/) offers free online storage for Docker repositories.
The Docker manual [explains](https://docs.docker.com/engine/getstarted/step_five/) how to get an account and push your Docker images to it.
