# How to document your work and insights

You who is reading the set of documents in this directory of the [Brendel Group Handbook](https://github.com/BrendelGroup/bghandbook) may be wondering how we produce such nice documentation.
Here we review several components of this question:
 - how to edit documentation
 - how to determine the scope of documentation
 - how to keep records of your UNIX commandline work

## Markdown documents
Most of the documents in the handbook are prepared using the [Markdown](http://daringfireball.net/projects/markdown/) text-to-HTML conversion tool.
The Markdown syntax is easy to learn and unobstrusive (reading a Markdown document as plain text is not a hardship).
But more to the point, it allows you to produce a nice-looking document when viewed at GitHub or with a Markdown viewer.
Please take a few minutes to learn all you need by following the [Mastering Markdown - GitHub Guide](https://guides.github.com/features/mastering-markdown/).
One nice editor and viewer for Markdown documents is [Atom](https://atom.io/); there are many other options.
On our Fedora machines we used the following commands to install this editor:

```
sudo dnf install dnf-plugins-core
sudo dnf copr enable helber/atom
sudo dnf update
sudo dnf install atom
```

Follow the installation instructions at the [Atom](https://atom.io/) project site for other systems.
The Fedora instructions provided above are a good example of useful documentation!

## What should be documented
The typical answer to a question as broad as "what should be documented" is the laconic "depends."
The bottom line is that our handbook should be useful.
There is little point in duplicating excellent and easily available resources.
But for some topics, a quick summary and pointers to other resources, conveniently available to us in one place, will be hugely helpful - both to direct new group members and students to what operational knowledge and skills they need to acquire (and do so quickly) and also for future reference (few of us remember everything we ever learned).
Thus we will make selections based on experience.
We will keep the handbook as concise as possible and as comprehensive as necessary.
Group members are strongly encouraged to contribute draft documentation on topics of common interest.
Our editorial board will be happy to review contributions and expand our repository consistently with the stated goals of our handbook project.

There is another aspect to the topic of documentation which involves record keeping of your own computational work.
You may find some of the examples in the handbook very useful in this respect, too.
See next section!

##  Annotated history of UNIX commandline work
It is absolutely critical that you develop impeccable record keeping of your computational work.
First, such habit will save you much time over the course of your projects.
Invariably, you will revisit what you have done before, either to remind yourself of particular work or to adapt that work for a new task.
Second, sharing precise command records is the __only__ way to unambiguously communicate to the rest of the group (and the world) what you have done.
And third, your records may well become the launching point for one of the group's [RAMOSE](https://github.com/BrendelGroup/BWASP) workflows!

One of the simplest ways of keeping good records is to make use of the UNIX _history_ command.
Let's look at the last few commands the author of this document issued to edit this file:

```
...
1001  cd bghandbook
1002  swd
1003  git pull origin master
1004  cd doc
1005  swd
1006  cp 02-Howto-UNIX.md 03-Howto-WriteDocumentation.md
1007  vi 03-Howto-WriteDocumentation.md
1008  atom 03-Howto-WriteDocumentation.md
1009  git add 03-Howto-WriteDocumentation.md
1011  git commit -m "first draft of 03-Howto-WriteDocumentation.md"
1012  git push origin master
1013  git pull origin master
```

Typically, one's history does not look that clean (and admittedly, the above was a bit edited to fit the current needs), but something like the above will be produced by the _history_ command, with the numbers in the first column numbering consecutive command and the second column showing the commands as sent to the operating system.
We can turn this rough draft into a nicer draft very quickly:

```
history | tail -n 14 | cut -c8- > myrecord
vi myrecord
```

The above pulls out the last 14 lines of the history, then drops the first 7 characters (the meaningless numbers), and writes the result to file _myrecord_, which you can then edit (e.g., with _vi_).
An annotated record might look like this

```
# Go to my bghandbook git clone:
#
cd bghandbook
swd
# Make sure everything is up to date:
#
git pull origin master
cd doc
swd
# Use an existing document as a template and do some initial editing:
#
cp 02-Howto-UNIX.md 03-Howto-WriteDocumentation.md
vi 03-Howto-WriteDocumentation.md
# Fine editing with atom to check on Markdown rendering:
#
atom 03-Howto-WriteDocumentation.md
# Well done job gets committed, pushed, and current status checked:
#
git add 03-Howto-WriteDocumentation.md
git commit -m "first draft of 03-Howto-WriteDocumentation.md"
git push origin master
git pull origin master
```

Often this edited file could be left in the directory as _0RECORD_ or even _0README_.
If the record consists of various commands that should be executed in that order, then a file like the one above with all comments started with the _#_ sign can even work as a script: _source 0RECORD_ will execute the non-comment lines in the file in that order in the _bash_ shell.
Thus, your entire work will be reproducible (obviously, for the above this is only partly true because the content of the editing is not recorded in this example; more pertinent examples will be documented elsewhere).
