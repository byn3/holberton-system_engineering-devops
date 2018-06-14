# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---

**What Is “The Shell”?**  
*The Shell delivers keyboard inputs to the OS to perform. They were the precursors to GUIs and bash is one of the most popular.*  

**What is the difference between a terminal and a shell?**  
*Shell processes commands and returns output. Terminals run shell programs.*  

**What is the shell prompt?**  
*It is where the user types commands. The shell prompt is also known as the command line. On Vim it is when you type colon (:).*  

**How to use the history?**  
*Up arrow. Greatest shortcut for bash.*  

**What do the commands or built-ins cd, pwd, ls do?**  
*cd is change directory, follow it with the directory name. pwd is print your current working directory. ls is list current directory. Yes, these sentences bothered me cause I wanted to capitalize the first letter but you can't type Cd or Pwd.*  

**How to navigate the filesystem?**  
*cd, ls, cd, ls... throw in 'ls -a' to see hidden files.*  

**What are the . and .. directories?**  
*. is current and .. is parent.*  

**What is the working directory, how to print it and how to change it?**  
*The working directory is the current folder you are in. pwd is to change and refer above how to navigate or change it.*  

**What is the root directory?**  
*The root is the highest or top directory in the hiearchy, it contains all other files.*  

**What is the home directory, and how to go there?**  
*Say this in E.T.'s voice, "cd go home." The home dir is the login directory, or the repo of the user's personal files. It is usually the first one you are inside once logging into the system.*  

**What is the difference between the root directory and the home directory of the user root?**  
*The home directory is in the root. The root is king of all. Root is topmost level, referred by '/.' while home is the user and has folders like Documents or Music or Pictures and is referred to by '~'.*  

**What are the characteristic of hidden files and how to list them?**  
*They begin with a '.' usually and they are listed with the -a flag.*  

**What does the command cd - do?**  
*cd - brings your back to the previous directory.*  

**What do the commands ls, less, file do?**  
*ls lists the files and dir in the current working dir. less views the file instead of opening them. file shows the type of data contained in a computer file.*  

**How do you use options and arguments with commands?**  
*You would use the option indicator '-' and that would allow the use of flags. Arguments, or parameters, are the targeted file names or dir or other stuff you are trying to manipulate. Extra C facts (argc contains the number of arguments passed from the command line and argv contains the pointer to strings containing the names of these arguments).*  

**Understand the ls long format and how to display it?**  
*la -l. The long format shows the file permissions, owner, group, size in bytes, modification time, and file name.*  

**What does the ln command do?**  
*It creates a hard link to an existing file. If it has the flag -s then it is a symbolic link. This allows multiple filenames to be*  

**What do you find in the most common/important directories?**  
*[Answer in this link](http://www.dba-oracle.com/linux/important_files_directories.htm). We got all the good stuff in this link, scroll down to important directories. Theres boot which helps boot the process and kernel, bin with its binary stuff, tmp, usr, and tons of other important ones*  

**What is a symbolic link?**  
*Also known as soft link or symlink. This is a term for any file that contains a reference to another file or dir in the form of an absolute or relative path. Basically it makes text string that is connected to a target and it is like a pointer. Symbolic links can point to non-existant files.*  

**What is a hard link?**  
*Hard links cannot point to nothing. They must always refer to an existing file. Hard links .*  

**What is the difference between a hard link and a symbolic link?**  
*Hard is hard. Really connected. If the original goes so does the hard link. For symbollic, there can be an orphaned or dangling link. Symbolic links can exist on their own and arn't completely dependent on the target file for existing*  

**What do the commands cp, mv, rm, mkdir do?**  
*cp copies. mv moves or renames. rm removes files or directories. mkdir makes directories.*  

**What are wildcards and how do they work?**  
*The asterisk, or star, or multiply sign, is a wild card. Anything can be put in. It can be everything or anythinng. It can be super specific if you follow proper syntax or regex stuff.*  

**How to use wildcards?**  
*Star card is most common. It cna be anything, even zero chars. the question mark wild card means that can be any one single character. So c?t can be cat or cot or cut. Square brackets wild cards are any of the caracters inside the bracket. So common uses are vowels \[aeiou]. Hyphens inside mean include inbetween like a-g means a through g. \[a-dog]* would mean to look for anything that stats with a through d or begins with o or g.[0-9][0-9][0-9] looks for all 3 digit numbers.*  

**What do type, which, help, man commands do?**  
*type displays information about command type. which shows full path of commands. help shows a ton of different commands. Typing in help onto the command line is self-explanatory. man shows manuals. type man and it will prompt which page number.*  

**What are the different kinds of commands?**  
*Type "type type" or "type alias" to see different types. Some might be a shell builtin, others are locaed in important directories.*  

**What is an alias?**  
*A command that enables a replacement of a word by another string. Common for abbreviating a system command.*  

**When do you use the command help instead of man?**  
*help is a bash command. It uses internal bash structures to store and retrieve info about bash commands. man is a macro that uses troff (geoff). The output of processing a file is sent to a pager by the an by default. info is a text-only viewer for archives in the output format of Texinfo*  

**How to read a man page?**  
*NAME is the name of the command or function, followed by a short description. SYNOPSIS is a formal description of how to run it and what command line options it accepts. Usually a list of arguments and which header file contains the definition.*  

**What are man page sections?**  
*.*  

**What are the section numbers for User commands, System calls and Library functions?**  
*.*  

**Keyboard shortcuts for Bash?**  
*.*  

**Common shortcuts for Bash?**  
*.*  

**LTS?**  
*.*  

**What does LTS mean?**  
*.*  

**What does RTFM mean?**  
*.*  

**What is a Shebang?**  
*.*  

Requirements
Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 14.04 LTS
All your scripts should be exactly two lines long ($ wc -l file should print 2)
All your files should end with a new line (why?)
The first line of all your files should be exactly #!/bin/bash
A README.md file, at the root of the folder of the project, describing what each script is doing
You are not allowed to use backticks, &&, || or ;
All your scripts must be executable. Use this command: chmod u+x file. We will see later what it means.
