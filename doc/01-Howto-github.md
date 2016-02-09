# 01-Howto-github

If you got to this document, then you are on a good way - you must have learned that 1) the [Brendel Group](https://github.com/BrendelGroup/) is using __github__ to disseminate our bioinformatics software; and 2) we are using __git__ to manage our collaborative projects.
Presumably you are a group member.
Read on if you are new to the group - the documentation in this __Howto__ explains everything you need to know to get going.
Everyone else might find helpful reminders - or ways to expand or improve our documentation.
After all, this is all about collaboration.

## Git basics

There are many excellent resources on the internet, ranging from basic tutorials that teach you the basics of git in less than an hour to full documentation and user forums that explain advanced use of __git__.

One of the best beginner's tutorials is [git-tutorial.pdf](http://www.cs.columbia.edu/~sedwards/classes/2013/4840/git-tutorial.pdf) by instructors at Columbia University.
Follow the examples, play with the commands, and within the hour you will have learned the basic concepts and commands.

When you are ready for more, take a look at [A Quick Introduction to Version Control with Git and GitHub](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668); and finally delve into
the [Pro Git book](https://git-scm.com/book/en/v2) (when you feel like you should work like a pro).

To work with __github__, you need to set up an [account](https://github.com/join) first.

## The creative triangle

There are many repositories owned by the [Brendel Group](https://github.com/brendelgroup/) organization, each corresponding to a distinct project.
For each project on which you are collaborating, there is going to be the same structure and process as we will explain for this repository, the [Brendel Group Handbook](https://github.com/BrendelGroup/bghandbook).

There are three copies of the repository that you will need to track and navigate.
At the apex of your creative triangle is is the "__upstream__" repository which refers to the edited and approved version of the handbook as available in the Brendel Group owned [repository](https://github.com/BrendelGroup/bghandbook).
At the base of the triangle are your personal __fork__ of the repository, referred to as "__origin__" and a __clone__ of the repository which we'll refer to as "__sandbox__".
Your __sandbox__ will typically reside on your personal computer, let's say your laptop.
That's where you play with new ideas, be these documentation files or code.

Setting up your __origin__ and __sandbox__ spaces could hardly be simpler: on the [upstream](https://github.com/BrendelGroup/bghandbook) github site, follow the instructions under the __Fork__ button.
Once you have your __fork__, you will see the address for creating a clone (e.g., https://github.com/vpbrendel/bghandbook.git for user _vpbrendel_).  On your computer, move to the desired directory and download your new clone (replace the address with the one provided from your fork):
```bash
[]git clone https://github.com/YOUR_USERNAME/bghandbook.git
```

### From __sandbox__ to __origin__

If you have set up your __sandbox__ clone in your local __bghandbook__ directory, you should see something like the following (_vpbrendel_ will be replaces by your own __github__ user name):

```bash
[]git remote -v
origin	https://github.com/vpbrendel/bghandbook.git (fetch)
origin	https://github.com/vpbrendel/bghandbook.git (push)
```

Edit and add documents, commit your changes as you have learned in the __git__ tutorial, and when you are ready, __push__ your changes to your __origin__ repository:

```bash
[]git push origin master
```

Then view your changes at your __fork__ repository on __github__.

### From "__origin__" to "__upstream__"

If you are happy with how the changes you pushed from your __sandbox__ to __origin__ came out, then you presumably would want to pass on your contribution to the __upstream__ master repository.
To do this, you initiate a _pull_ request at the website of your __origin__ repository.
The __upstream__ administrators will review your request and merge acceptable contributions into the master copy.
Thank you!

### Syncing your __origin__ fork with the __upstream__ repository

To complete the creative triangle, we need to be able to bring our own __origin__ repository up to date with respect to other changes that may have been accepted into the __upstream__ repository - after all we want to work as a team, and thus we won't be the only ones contributing.
To do this, you will need to first update your __sandbox__, then push those updates to your __origin__ repository.
Continuing with our example:

```bash
[]git remote add upstream https://github.com/brendelgroup/bghandbook
[]git remote -v
origin	https://github.com/vpbrendel/bghandbook.git (fetch)
origin	https://github.com/vpbrendel/bghandbook.git (push)
upstream	https://github.com/brendelgroup/bghandbook (fetch)
upstream	https://github.com/brendelgroup/bghandbook (push)
[]git fetch upstream
[]git branch -va
...
[]git checkout master
...
[]git merge upstream/master
...
[]git push origin master
```

As you can see, all sides of the triangle correspond to paths being traveled at.
After a while, these will be well-trodden paths for you!
