# Basic UNIX Shell Tutorial

The book <u>Bioinformatics Data Skills</u> by Vince Buffalo (available on [Amazon](http://www.amazon.com/Bioinformatics-Data-Skills-Reproducible-Research/dp/1449367372/) and [O'Reilly Books](http://shop.oreilly.com/product/0636920030157.do)) offers a great chapter on the UNIX shell (the "command line").
The level of this material is intermediate, however, and assumes that the reader has basic proficiency with the shell.
If you are just beginning to learn the UNIX shell, the following tutorial (or any number of others you can find with a [simple Google search](https://www.google.com/#q=linux+command+line+tutorial)) may provide a gentle transition to the level of material covered in <u>Bioinformatics Data Skills</u>.

**Note**: Computers running Linux or Mac OS X operating systems can be considered *UNIX machines*.
Although there are some subtle differences between Mac and Linux (and even between different flavors of Linux), basic UNIX functionality should be consistent across these different operating systems.
The Windows/DOS shell is a different beast entirely, which we will not cover at all here.

## The Shell

The most common and most powerful method of interacting with a UNIX machine is through the shell (sometimes called the *command line* or *command prompt*, accessed through a *terminal* window).
The basic idea behind the shell is pretty simple—you enter a command into the terminal, and the shell executes that command.
Sometimes a command will print some text back to your terminal, and sometimes it will modify or create or delete files.
This tutorial will give you an introduction to the types of commands you will need to know to navigate through the file system and run the scientific software.

## Moving around

Files on any computer are stored in a nested directory structure.
When you use a Mac or Windows computer, you have probably learned to click on folders to open them, and to continue clicking on the additional sub-folders until you have located the file you are looking for.

When using the shell, you navigate through the file system a bit differently.
When you open your terminal window, you start at a default location called your *home directory*.
You then use the `cd` command to change your location—analogous to clicking on a folder on Mac or Windows.

Whenever the prompt is open, you can type the `pwd` command to show your current location (`pwd` is short for *print working directory*).
If I open a terminal on my UNIX machine and type *pwd*, it will show me the location of my default directory.

```
[standage@localhost ~]$ pwd
/home/standage
[standage@localhost ~]$
```

The `pwd` command printed `/home/standage` as my current location.
That means by default, my command prompt is in a directory called `standage`, which is inside of another directory called `home`, which is at the root of the file system.
To see the files in this directory, I can use the `ls` command.

```
[standage@localhost ~]$ ls
Desktop
[standage@localhost ~]$
```

It looks like the only file in my home directory is another directory called `Desktop`.
If I want to go to that directory, I use the `cd` command (short for *change directory*).

```
[standage@localhost ~]$ cd Desktop
[standage@localhost Desktop]$
```

You can see that the command did not print out any output like the previous ones did, but now my prompt looks different.
Before, it showed `~` as my current location, but now it shows `Desktop`.
As you navigate around the file system, your prompt may be updated to reflect your location.
Remember, you can always figure out where you are by typing the `pwd` command.

If I want to go back to my home directory, I can do this in several ways.
  * The symbol `~` is a shortcut for my home directory. I can go to my home directory at any time using the command `cd ~`.
  * The symbol `..` represents the parent directory of the current directory. For example, if I am in the directory `/home/standage/Desktop`, then `..` corresponds to `/home/standage`, `../..` corresponds to `/home`, and `../../..` corresponds to the root directory `/`. Another way to get to my home directory from `/home/standage/Desktop` is to use the command `cd ..`.
  * If you enter the command `cd` without any file or directory name after it, the command will take you back to your home directory.

```
[standage@localhost Desktop]$ cd ~
[standage@localhost ~]$ pwd
/home/standage
[standage@localhost ~]$ cd /usr/lib64/httpd/modules/
[standage@localhost modules]$ pwd
/usr/lib64/httpd/modules
[standage@localhost modules]$ cd ..
[standage@localhost httpd]$ pwd
/usr/lib64/httpd
[standage@localhost httpd]$ cd ../..
[standage@localhost usr]$ pwd
/usr
[standage@localhost usr]$ cd
[standage@localhost ~]$ pwd
/home/standage
[standage@localhost ~]$
```

## Tab completion

If you want to save time when typing long directory or file names, start typing the first 2 or 3 letters of the directory and then hit the `Tab` button.
This will autocomplete (fill in) the rest of the directory/file name for you.
If more than one directory starts with those 2 or 3 letters, then it will fill in as much as it can automatically.
This will save you a lot of time and help prevent typos.

## Commands

### Path configuration

When you type a command like `ls` or `pwd` or `cd`, you are actually running a program.
There is a special program file in some directory on your computer called `ls`, and when you enter the `ls` command your computer executes that program.

How does your computer know where to find the `ls` program (or any other program command you type)?
There is a setting on your computer called your *path*--it is a list of directories on your computer.
When you type in the `ls` command, your computer looks at all the directories in your path until it finds a program called `ls`, and then it executes it.
You will need to remember this when you begin compiling programs on your VM.
If you do not copy your program into a path folder or update your path settings, then your computer will not know how to find and execute the program you just installed.

### Redirecting output

Many programs will print output to your screen.
When you enter the `pwd` command, the output is a single line of text showing current directory.
However, some commands may print thousands of lines--more than can fit on your screen.
How do you manage the output?

One way is to redirect the output to a file using the `>` character.

```
[standage@localhost ~]$ cd /usr/bin
[standage@localhost bin]$ ls > ~/newfile.txt   # Save the output to a new file
[standage@localhost bin]$ wc -l ~/newfile.txt  # Count the lines in this new file
1672 /home/standage/newfile.txt
[standage@localhost bin]$
```

There are 1672 files in the `/usr/bin` directory.
If we simply typed in `ls` without redirecting the output to a file, it would have overloaded the screen!

Another common approach in UNIX is to "pipe" programs together.
If you place a pipe "|" character between two programs, then the terminal will use the output of the first program as the input for the next program.
For example, we can pipe the `ls` output into the `grep` program to select only those lines that contain "eat".

```
[standage@localhost bin]$ ls | grep eat
create-branching-keyboard
create-jar-links
euca-create-snapshot
euca-create-volume
[standage@localhost bin]$
```

If you want to or need to, you can use multiple pipes in a single command.
In each case, the output from the former command will be used as input for the latter command.

### Command history

In the command prompt, you can use the up and down arrows on your keyboard to search through commands you have entered previously.
If you want to see your entire (recent) command history, type `history`.
This could be a lot of output, so you may want to redirect it to a file or pipe it into grep to search for a specific command.

### Manuals

If you forget how to use a command, there are manuals (or "man pages") available on your system to remind you.
To see the manual for `grep`, type `man grep`.
You can use your up and down arrows to scroll, and then just hit `q` when you're done.

### File management

Now that you've got the basics down, I will use a lot less words and simply demonstrate by example.
Remember that UNIX filenames are case-sensitive (in other words, "Desktop" is not the same as "desktop").

### Copying files and directories

```
[standage@localhost bin]$ cd
[standage@localhost ~]$ ls
Desktop  newfile.txt
[standage@localhost ~]$ cp newfile.txt anotherfile.txt        # Create a copy of 'newfile.txt' called 'anotherfile.txt'
[standage@localhost ~]$ ls                     
Desktop  anotherfile.txt  newfile.txt
[standage@localhost ~]$ ls Desktop/
idrop.desktop
[standage@localhost ~]$ cp newfile.txt Desktop                # Create a copy of 'newfile.txt' and place it in the 'Desktop' directory
[standage@localhost ~]$ ls Desktop/
idrop.desktop  newfile.txt
[standage@localhost ~]$ cp newfile.txt Desktop/crazyfile.txt  # Create a copy of 'newfile.txt' called 'crazyfile.txt' and place it in the 'Desktop' directory
[standage@localhost ~]$ ls Desktop
crazyfile.txt  idrop.desktop  newfile.txt
[standage@localhost ~]$ cp -r Desktop anotherDirectory        # Create a copy of the 'Desktop' directory and all its contents and call it 'anotherDirectory'
[standage@localhost ~]$ ls
Desktop  anotherDirectory  anotherfile.txt  newfile.txt
[standage@localhost ~]$ ls anotherDirectory
crazyfile.txt  idrop.desktop  newfile.txt
[standage@localhost ~]$
```

### Moving and renaming files and directories

```
[standage@localhost ~]$ ls
Desktop  anotherDirectory  anotherfile.txt  newfile.txt
[standage@localhost ~]$ mv newfile.txt oldfile.txt            # Rename 'newfile.txt' to 'oldfile.txt'
[standage@localhost ~]$ ls
Desktop  anotherDirectory  anotherfile.txt  oldfile.txt
[standage@localhost ~]$ mv oldfile.txt anotherDirectory       # Move 'oldfile.txt' to the directory 'anotherDirectory'
[standage@localhost ~]$ ls
Desktop  anotherDirectory  anotherfile.txt
[standage@localhost ~]$ ls anotherDirectory
crazyfile.txt  idrop.desktop  newfile.txt  oldfile.txt
[standage@localhost ~]$ mv anotherDirectory Desktop           # Move the directory 'anotherDirectory' into the directory 'Desktop'
[standage@localhost ~]$ ls
Desktop  anotherfile.txt
[standage@localhost ~]$ ls Desktop
anotherDirectory  crazyfile.txt  idrop.desktop  newfile.txt
[standage@localhost ~]$
```

### Creating an empty directory

```
[standage@localhost ~]$ ls               
Desktop  anotherfile.txt
[standage@localhost ~]$ mkdir testDirectory
[standage@localhost ~]$ ls
Desktop  anotherfile.txt  testDirectory
[standage@localhost ~]$ ls testDirectory
[standage@localhost ~]$
```

### Deleting files and directories

Be careful...by default, UNIX will not ask you if you are sure you want to delete the file.
Once you delete it, it's gone.
No recovery from Recycle Bin or Trash or anything like that.

```
[standage@localhost ~]$ ls
Desktop  anotherfile.txt  testDirectory
[standage@localhost ~]$ rm anotherfile.txt    # Delete file
[standage@localhost ~]$ ls
Desktop  testDirectory
[standage@localhost ~]$ rm -r testDirectory/  # Delete directory
[standage@localhost ~]$ ls
Desktop
[standage@localhost ~]$
```

### Viewing files

  * `less`: will display the file; use up/down arrows to scroll, f/b to page, q to quit
  * `head`: print the first 10 lines of the file to the terminal; use `head -n x` to print the first x lines of the file
  * `tail`: print the last 10 lines of the file to the terminal

### Editing files

  * `nano`: not very popular, but probably the simplest for beginners; command hints are shown at the bottom of the screen
  * `vi` and/or `vim`: popular text editor, but different editing modes can be confusing at first
  * `emacs`: also popular, but it has its own quirks

Beware! Many professional programmers often have very strong feelings about which text editor is best.
My favorite is `vim`, but `nano` is probably the simplest and best option for beginners.

### Archives and compression

Sending large data files or programs over the internet can take a long time, so to speed the process up files are often compressed.
Zip archives (files with a `.zip` extension) are quite common, but there are a few others you will frequently see with UNIX.
Depending on the type of compression used, you will need to use a different command to decompress and access the files.

|   Extension             |    Command    |   Example   |
|-------------------------|---------------|--------------------------------------|
|   `.zip`                |  `unzip`      |  `unzip myfiles.zip`                 |
|   `.bz2`                |  `bunzip2`    |  `bunzip2 allMySequences.fasta.bz2`  |
|   `.gz`                 |  `gunzip`     |  `gunzip allMyGenes.gff3.gz`         |
|   `.tar`                |  `tar`        |  `tar xf myDirectory.tar`            |
|  `.tar.gz` or `.tgz`    |  `tar`        |  `tar xzf myProgram.tar.gz`          |
|  `.tar.bz2`             |  `tar`        |  `tar xjf myApp.tar.bz2`             |

## Installing software
Some software can be run directly from plain text files—these are typically called "scripts" (Perl, Python, bash, etc).
However, many software applications have source code that must be compiled into a executable binary file before it can be run.
This is the case with most of the software we will be using this semester.

The first step to installing software on your UNIX machine is to download the source code, using either your web browser or a command like `wget` or `curl`.
If necessary, you will need to decompress the source code.
If you downloaded the program from a web page, then that page probably includes installation instructions as well.
However, it is common for installation instructions to be included with the source code as well.
They are usually kept in files called `README` or `INSTALL` or something like that.
You should follow the instructions in these files to install the software.
A very typical installation process goes as follows.

```
./configure
make
sudo make install
```

This isn't universal, but it is very common and you will see it come up frequently in this course.
Each of these commands will generally print *a lot* of output to the terminal.
Don't worry about trying to read it all, you can ignore most of it.
However, if there is a problem, hopefully the last few lines of output will make that clear.
The more experience you get with this, the easier it will be to recognize.

Take a look at the terminal recording below for a simple example of a typical software installation.
<script type="text/javascript" src="https://asciinema.org/a/2077.js" id="asciicast-2077" async></script>
