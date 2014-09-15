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
- **Do not maintain multiple versions of your repository!** This defeats the whole purpose of having version control in the first place, and in doing so you risk overwriting your work. Of course, it's perfectly fine to have a copy of your git repository on your work computer and another copy on your home computer, so long as you keep them synchronized (via SSH or using a 3rd remote repo on GitHub). But if you have two copies of the repo on your work computer--``myproj`` and ``myproj-testing``, for example--then you are almost certainly Doing It Wrong.™ If you feel the need to do so, take a look at [Git's branching features](http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging).
- Do not store one Git repository within another Git repository.
- Storing large data files in a Git repository is usually not a good idea. If you need large data files for automated testing or for a particular analysis, the best approach is the following.
    - If the data files are not already accessible from a public database like GenBank or SRA, post them on the BrendelGroup website or upload them to a research data repository such as [fig<b>share</b>](http://figshare.com/).
    - Include a script in your Git repo to automatically download the data files.
    - Add the data files to your repo's ``.gitignore`` file to explicitly prevent them from being tracked by Git.

## Hosting

Coming soon!

## Bug tracking

Coming soon!

## Backup

Coming soon!

## Testing

Coming soon!

## Collaboration

Coming soon!
