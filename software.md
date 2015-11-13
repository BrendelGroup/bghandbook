# Brendel Group: software development and distribution
Last update: Daniel S. Standage, 13 November 2015

The Brendel Group's research focus lies at the intersection of genome biology and data science.
Software is an integral part of the work we do, and although most group members have little or no formal software engineering experience, we recognize the value of enforcing some basic software engineering best practices.

This document outlines the Brendel Group's standard operating procedures with respect to developing and distributing research sofware.

## Version control

Placing all research projects—and especially research software—under version control is crucial for reproducible research.
Version control systems are designed to facilitate the development of your project over time, keeping your working environment uncluttered while at the same time maintaining a full searchable history of the entire project.
Version control systems can also be integrated with online hosting systems that facilitate backup, distribution, and collaboration for your project.

We use the Git version control system in the Brendel Group.
If you are unfamiliar with Git, a beginner's tutorial is available [here](https://try.github.io).
Here are some general recommendations.

- Begin taking snapshots (commits) of your project as early as possible: ideally, from the project's inception.
- Focus on small, frequent commits rather than large, infrequent commits. Ideally, there shouldn't be huge sweeping changes to the code between each commit. If implementing new features or fixing bugs *does* require extensive changes to existing code, this suggests that the code should probably be refactored.
- **Do not maintain multiple versions of your repository!** This defeats the whole purpose of having version control in the first place, and in doing so you risk overwriting your work. Of course, it's perfectly fine to have a copy of your git repository on your work computer and another copy on your home computer, so long as you keep them synchronized (e.g. via GitHub). But if you have two copies of the repo on your work computer—``myproj`` and ``myproj-testing``, for example—then you are almost certainly Doing It Wrong™. If you feel the need to maintain two different copies of your repo, you should probably take a look at [Git's branching features](http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging) instead.
- Do not store one Git repository within another Git repository.
- Storing large data files in a Git repository is usually not a good idea. If you need large data files for automated testing or for a particular analysis, the best approach is the following.
    - If the data files are not already accessible from a public database like GenBank or SRA, post them on the Brendel Group website or upload them to a research data repository such as [fig<b>share</b>](http://figshare.com/).
    - Include a script in your Git repo to automatically download the data files.
    - Add the data files to your repo's ``.gitignore`` file to explicitly prevent them from being tracked by Git.

## Hosting

Several code hosting and publishing services exist, and all are free for open source software.
In addition to hosting Git repositories, these services provide a variety of other useful features: wikis, bug/issue trackers, usage statistics, forks, and pull requests, to name a few.

We use the [GitHub hosting service](http://github.com) in the Brendel Group.
Group members have individual GitHub accounts, but are also added to the **BrendelGroup** GitHub organization and given access to projects on which they are collaborating.

- Software hosted on GitHub should be considered *development* code. This essentially means that while the software is working correctly in the developer's hands, a bit more work may be needed to ensure that the software compiles/runs correctly on other systems and produces the correct results.
- Git provides a mechanism for [tagging snapshots of your code](https://git-scm.com/book/en/v2/Git-Basics-Tagging), and this should be used to tag stable software releases. GitHub recognizes tags in your repository and publishes these on a **Releases** page with options to download `.zip` or `.tar.gz` archives of the repository.
    - Note: some extra work typically goes into the intial stable release.
        - there needs to be sufficient documentation so that a scientist with basic computing skills can run the software
        - the software should run (and compile, if necessary) on most/all UNIX machines
        - the software should be accompanied by one or more test data sets to validate that the software works correctly
    - Once the initial stable release is made, subsequent stable releases typically require less tedious work.
- The http://brendelgroup.org Bioinformatics2Go pages provide a secondary location to store and advertise stable software releases. Coordinate with Volker to host releases here.

## Bug tracking

GitHub automatically creates an issue tracker for each repository it hosts.
The issue tracker can manage bug reports, feature requests, questions, and tasks lists, and is an excellent tool for collaboration and community engagement.
The Brendel Group discourages use of independent bug tracking software and endorses the use of GitHub's issue tracking features for software development.

## Backup

All research projects, whether they involve software development or not, should have a regular backup procedure.
Software projects should be syncronized frequently with GitHub, which gives a single point of backup.
The ``/DATA/GROUP`` partition, which is mounted to each of the Brendel Group's research VMs, can also be utilized for backup, as data stored there is protected by redundant backup.
Secondary backup options include the iPlant Data Store, file hosting services like Box or Dropbox, or an external hard drive.

## Testing

Testing is the process by which you verify that your software actually does what it's intended to do.
You should think about testing at a very early stage in the software development process.
Ideally you would have tests prepared before a single line of code has been written, although this is admittedly a pretty high bar.
It is very reasonable, though, to expect testing while the software is still in an early prototype.

The Brendel Group requires testing for all software development projects and endorses the following best practices.

- When possible, start with very small test data sets for which you can compute the correct answer using pen and paper. Go ahead and compute the answer **before running the test** to avoid biasing the test! It is ok to create small artificial data sets for testing, although when possible these should always be followed later by testing with full-size real data sets.
- Unless you have a very good reason, all tests should be automated. For example, if your testing procedure involves running a set of 4 commands, you need to record that testing procedure somewhere: a README file, a wiki, etc. It does not take much additional work to place those 4 commands in a shell script or Makefile so that the testing procedure can be automated with a single command.
- With the exception of small scripts and programs, most source code is organized into functions/subroutines/methods and  modules/classes. And when a software package includes more than one program, its common that a function or module is used by more than one program. There is a need to test at both levels.
    - **Unit testing** is making sure that a particular function or class is behaving as expected. In unit testing, you should think of yourself in the role of a *software developer* and design the tests to make sure that you and other software developers can use each function or class with confidence.
    - **Functional testing** is making sure that your program or programs behave as expected. In functional testing, you should think of yourself in the role of a *scientist* or *end users* and design the tests to make sure that you and other end users can use each program with confidence.
- GitHub offers seamless integration with the [Travis CI service](https://travis-ci.org/). If your tests are automated in a script or Makefule (they should be!) then you can integrate with Travis by activating the TravisCI webhook in GitHub and adding a ``.travis.yml`` configuration file to your repository. Once configured, every time you push a new commit to GitHub Travis will download your code, run the tests, and alert you if there are any errors.

## Collaboration

Git and GitHub make it easy for multiple multiple group members (or collaborators) to actively work on the same software development effort.
For projects involving multiple active contributors, the Brendel Group uses the [GitHub flow](https://guides.github.com/introduction/flow/index.html) model for collaborative development.

- The primary repository for the project is owned by the **BrendelGroup** GitHub organization, and each contributor maintains their own fork. For example, if the project is called ``RNASeqer``, then the main repo will be at ``BrendelGroup/RNASeqer`` while group members ``alice`` and ``bob`` will have their own forks at ``alice/RNASeqer`` and ``bob/RNASeqer``.
- Each active contributor maintains a local clone of their fork on their workstation(s) and uses ``git push`` and ``git pull`` to syncronize with their fork on GitHub.
- When a contributor wishes to integrate their work with the primary repository, they use GitHub's pull request feature. This gives other active contributors a chance to review the changes, evaluate new testing procedures (if any), and provide suggestions or other feedback. If the changes look good, another contributor will merge the pull request. If more work is needed, the pull request remains open and the contributor can continue adding new commits to the pull request until all concerns are addressed.
- When a project has multiple active contributors, **no one should accept their own pull requests**. Doing so could introduce unnecessary conflicts in the code. This requirement is not enforced by GitHub, so each contributor must regulate their own behavior in this regard.
