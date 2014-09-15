# Brendel Group: software development and distribution
Last update: Daniel S. Standage, 15 September 2014

The Brendel Group's research focus lies at the intersection of genome biology and data science.
Software development is an integral part of the work we do, and although most group members have little or no formal software engineering experience, we recognize the value of enforcing some basic software engineering best practices.

This document details the Brendel Group's standard operating procedures with respect to developing and distributing research sofware.

## Version control

Placing all research projects--and especially research software--under version control is crucial for reproducible research.
Version control systems are designed to facilitate the development of your project over time, keeping your working environment uncluttered while at the same time maintaining a full searchable history of the entire project.
Version control systems can also be integrated with online hosting systems that facilitate backup, distribution, and collaboration for your project.

We use the Git version control system in the Brendel Group.
If you are unfamiliar with Git, a beginner's tutorial is available **here** (link coming soon!).

- Begin taking snapshots (commits) of your project as early as possible: ideally, from the project's inception.
- Focus on small, frequent commits rather than large, infrequent commits. Ideally, there shouldn't be huge sweeping changes to the code between each commit. If implementing new features or fixing bugs *does* require extensive changes to existing code, this suggests that the code should probably be refactored.
- **Do not maintain multiple versions of your repository!** This defeats the whole purpose of having version control in the first place, and in doing so you risk overwriting your work. Of course, it's perfectly fine to have a copy of your git repository on your work computer and another copy on your home computer, so long as you keep them synchronized (via SSH or using a 3rd remote repo on GitHub). But if you have two copies of the repo on your work computer--``myproj`` and ``myproj-testing``, for example--then you are almost certainly Doing It Wrong.™ If you feel the need to maintain two different copies of your repo, you should probably take a look at [Git's branching features](http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging) instead.
- Do not store one Git repository within another Git repository.
- Storing large data files in a Git repository is usually not a good idea. If you need large data files for automated testing or for a particular analysis, the best approach is the following.
    - If the data files are not already accessible from a public database like GenBank or SRA, post them on the BrendelGroup website or upload them to a research data repository such as [fig<b>share</b>](http://figshare.com/).
    - Include a script in your Git repo to automatically download the data files.
    - Add the data files to your repo's ``.gitignore`` file to explicitly prevent them from being tracked by Git.

## Hosting

Several code hosting and publishing services exist, and all are free for open source software.
In addition to hosting Git repositories, these services provide a variety of other useful features: wikis, bug/issue trackers, usage statistics, forks, and pull requests, to name a few.

We use the [GitHub hosting service](http://github.com) in the Brendel Group.
Group members have individual GitHub accounts, but are also added to the **BrendelGroup** GitHub organization and given access to projects on which they are collaborating.

- Software hosted on GitHub should be considered *development* code. This essentially means that while the software is working correctly in the developer's hands, a bit more work is needed to ensure that the software compiles/runs correctly on other systems and produces the correct results.
- Stable software releases should be hosted on the http://brendelgroup.org site. A little bit of extra work typically goes into the intial stable release: there needs to be sufficient documentation so that a scientist with basic computing skills can run the software; the software should run (and compile, if necessary) on UNIX machines; the software should be accompanied by one or more test data sets to validate that the software works correctly. Once the initial stable release is made, subsequent stable releases typically require less groundwork.
- Git allows you to tag and label commits in your repository, and if you syncronize these tags with GitHub it will interpret them as releases. This provides a secondary mechanism for issuing stable software releases.

## Bug tracking

GitHub automatically creates an issue tracker for each repository it hosts.
The issue tracker can manage bug reports, feature requests, questions, and tasks lists, and is an important tool for community engagement.
The Brendel Group discourages use of independent bug tracking software and endorses the use of GitHub's issue tracking features for software development.

## Backup

All research projects, whether they involve software development or not, should have a regular backup procedure.
Software projects should be syncronized frequently with GitHub, which gives a single point of backup.
The ``/DATA/GROUP`` partition, which is mounted to each of the Brendel Group's research VMs, can also be utilized for backup, as data stored there is protected by redundant backup.
Secondary backup options include the iPlant Data Store, file hosting services like Box or Dropbox, or an external hard drive.

## Testing

Coming soon!

## Collaboration

Coming soon!
