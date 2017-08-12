# 01-Howto-Jetstream

Like many bioinformaticians, we are spending a lot of time installing software on our workstations.
If this does not sound familiar to you, then you likely not doing your job, and we need to have a chat.
But hang on: If you have finished reading this document, and then you are still spending a lot of time installing software, then you are doing something wrong, and we need to have a chat!
In short, this document is about solutions to the waste of time spent on setting up for your real work, particularly when that is a redundant effort, just repeating the struggles of the multitudes before you.
Your energy should be spent on new frontiers.

Let's review the typical scenario.
You need a particular software package, which luckily comes with nice installation instructions, but, unluckily, involves a bunch of prerequisites.
The prerequisites might include libraries that must be installed on the system; other software packages that must be downloaded and installed separately; and maybe some version of java, Perl modules, python packages, or R packages.
All of these might have prerequisites themselves, and thus the dependency tree can get large rather quickly.
Of course, package managers take care of a lot of these issues for us, but still, wouldn't we much rather just snap our fingers and be ready to get on with our research work?

As it were, virtual machines (VMs) are pretty close to the snap-your-fingers solution.
Here we review use of our __bgRAMOSE__ VM image, which is available through the NSF-funded [Jetstream](https://jetstream.cloud.org) project. 
Following along, you will have learned all you need to

* use an instance of __bgRAMOSE__ for your own research work
* contribute to the further development of __bgRAMOSE__
* use the __bgRAMOSE__ image as a means of documenting and disseminating code, workflows, and data analyses for your publications
* apply the same principles and approaches used in the __bgRAMOSE__ development to maintain your other workstations
* apply the same principles and approaches discussed here to document and disseminate all your computational work, performed anywhere


## Jetstream basics

Before we cna proceed, you'll need to have become familiar with some __Jetstream__ basics.
There is excellent documentation for this available:

* To use __Jetstream__, you will need an account and likely a rapid access trial allocation.  Please follow the posted [instructions](https://iujetstream.atlassian.net/wiki/display/JWT/Get+a+Jetstream+Rapid+Access+account).

* Once you have an account, you can log into __Jetstream__ via its [web interface](https://use.jetstream-cloud.org/).  Please review the posted [Quick Start Guide](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/29720582/Quick+Start+Guide).

* Although you will be able to access your VM via a __Jetstream__ provide web-based terminal, as a frequent user you will find ssh access more convenient.  Please see the posted [instructions](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/17465474/Adding+SSH+keys+to+the+Jetstream+Atmosphere+environment) to set this up.

* For a __bgRAMOSE__ VM, you can make use of its VNC/GUI/Desktop capacity and log in via an external VNC viewer.  This is so convenient that you might forget that you are working not on your laptop or local workstation but are using someone else's resource somewhere in the cloud!  Please see the posted [instructions](https://iujetstream.atlassian.net/wiki/display/JWT/Logging+in+with+VNC+desktop).


## Launching your __bgRAMOSE__ VM

Log into __Jetstream__ and take a look at your [Dashboard](https://use.jetstream-cloud.org/application/dashboard).
When you have some experience with __Jetstream__, you will want to look at the __Resources Used__ section and manage your allocation, or you might want to __Change your Settings__.
For now, click on __Launch New Instance__ and type __bgRAMOSE__ into the search field (of course, you are encourage to go back later and explore what other images are available).
Click on the top icon that comes, corresponding to the latest version, read the description and click __Launch__.
Edit the __Instance Name__ to your liking, select _m1.medium_ under __Instance Size__, and launch the instance.
Your screen will show the progress of the VM deployment.
You are ready for the next step once the screen indicates status __Active__ and provided an IP number.


## Customizing your __bgRAMOSE__ VM

Once you have an IP number for your VM, you are ready to access the machine.
If you have set up ssh (see above), you can access the machine in that way.
Simpler for now is to click on the VM icon in your __Instances__ list and follow the __Open Web Shell__ link on the righthand side; see what a [successful Web Shell login](https://iujetstream.atlassian.net/wiki/display/JWT/Logging+in+with+Web+Shell) should lool lik.
As we want to access the VM via VNC, we only have to login in this way once.
At the prompt type

```bash
[]sudo passwd <username>
```

where _<username>_ should of course be your Jetstream user name.
Set the password as you see fit.
Now you can __exit__ out of the __Open Web Shell__ and instead log into your VM via VNC, using the IP address followed by ":1" as address and your user name and password as just set on the commandline.
Now you should see a desktop screen like the following showing up:
![Image](./img/JetstreamVMvnc.PNG?raw=true)
Let's immediately customize the view.
Click on __Use default config__ and lauch a terminal from the icon in the bottom panel that will have shown up.
If I am on a big screen, I immediately adjust the desktop by entering a nifty command to change the screen size:
![Image](./img/JetstreamVMdesktop1.PNG?raw=true)
Furthermore, I prefer a different terminal default, and after __Edit__/__Preferences__/__Colors__/__Load Presets__ from the terminal top bar, selection __Black on White__, I am finally satisfied:
![Image](./img/JetstreamVMdesktop2.PNG?raw=true)

Well, actually, not quite, because I also like to have my familiar __bash__ aliases available, see my familiar directory structure, and have my __bash__ PATH variable correctly set for use.
After going over such setup steps for loads of VMs I have launched, I finally decided to streamline that process to a very simple protocol:

```bash
[]git clone https://github.com/vpbrendel/VMutil
[]more VMutil/xstartoverJS
```
as shown on the next screenshot:
![Image](./img/JetstreamVMdesktop3.PNG?raw=true)

Bottom line, excuting __VMutil/xstartoverJS__ sets up all my familiar environment.
In __VMutil/ulsUbuntu__ I find the file __paths2add__, and I dutifully put them into the right spot in my __~/.profile__ file:
![Image](./img/JetstreamVMdesktop4.PNG?raw=true)

Another

```bash
[]source ~/.profile
```

and the VM is really good to go.


## Using your __bgRAMOSE__ VM
Ok, what are we going to do with this nice VM now?
Any login terminal on your VM should provide the following lines

```bash
Welcome to your instance of Jetstream bgRAMOSE.
Please see /usr/local/share/bgRAMOSE/0README for helpful hints.
```

The next screenshot shows was we will see if we follow the hints:
![Image](./img/JetstreamVMdesktop5.PNG?raw=true)

Let's follow what the first lead, __/usr/local/share/bgRAMOSE/MMB/0README__.
This is a great example, following the T.R.Taylor & V.P. Brendel (2017) _Methods in Molecular Biology_ article describing our __GoRAMPAGE__/__TSRchitect__ workflow for the analysis of transcription start site (TSS) profiling experiments.
The instructions allow a user to completely reproduce the workflow described in the article, with all requisite software already pre-installed on their VM.
Once launched, your desktop might look like this
![Image](./img/JetstreamVMdesktop6.PNG?raw=true)

Ok, what did we say?
Time to go for a run, sleep, have lunch with your partner, whatever ...
Eventually, the job will finish.
Why?
Because you are on a VM where everything has been tested.
You are simply repeating what was done before.

Eventually, you go back to your VM desktop and can pull up results like this:
![Image](./img/JetstreamVMdesktop7.PNG?raw=true)


## So why is this a __big deal__?
What did we just achieve?
We reproduced a rather complex study, involving many steps of data acquisition, data processing, and statistical analysis of data.
Thus, we can truly discuss the merits of the approach and the authors' interpretation - but there is no ambiguity about what exactly they did.
It's right here - nothing hidden, nothing vague.
Ah, yes, that's __science__, you exclaim!
But, really, in your experience, how many published science articles ever live up to this standard, that everything should be _easily_ reproducible?
Is there any excuse in computational work for anything less?
No, certainly not in the age of virtual machines.
Jetstream __bgRAMOSE__ plainly leaves no wiggle room: put out your data work exactly as you describe it, and everyone shall be able to reproduce it.
Onward to the interesting questions: What does your study really show? What new insights does your data work provide?


## Appendix: Some fine points.

