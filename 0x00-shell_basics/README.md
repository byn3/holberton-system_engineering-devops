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
**What are the . and .. directories**  
*. is current and .. is parent.*  

**What is the working directory, how to print it and how to change it**  
*The working directory is the current folder you are in. pwd is to change and refer above how to navigate or change it.*  

**What is the root directory**  
*The root is the highest or top directory in the hiearchy, it contains all other files.*  

**What is the home directory, and how to go there**  
*Say this in E.T.'s voice, "cd go home." The home dir is the login directory, or the repo of the user's personal files. It is usually the first one you are inside once logging into the system.*  

**What is the difference between the root directory and the home directory of the user root**  
*The home directory is in the root. The root is king of all. Root is topmost level, referred by '/.' while home is the user and has folders like Documents or Music or Pictures and is referred to by '~'.*  

**What are the characteristic of hidden files and how to list them**  
*They begin with a '.' usually and they are listed with the -a flag.*  

**What does the command cd - do**  
*cd - brings your back to the previous directory.*  

**What do the commands ls, less, file do**  
*ls lists the files and dir in the current working dir. less views the file instead of opening them. file shows the type of data contained in a computer file.*  

**How do you use options and arguments with commands**  
*You would use the option indicator '-' and that would allow the use of flags. Arguments, or parameters, are the targeted file names or dir or other stuff you are trying to manipulate. Extra C facts (argc contains the number of arguments passed from the command line and argv contains the pointer to strings containing the names of these arguments).*  

**Understand the ls long format and how to display it**  
*la -l. The long format shows the file permissions, owner, group, size in bytes, modification time, and file name.*  

**What does the ln command do**  
*It creates a hard link to an existing file. If it has the flag -s then it is a symbolic link. This allows multiple filenames to be*  

**What do you find in the most common/important directories**  
*.*  

**What is a symbolic link**  
*.*  

**What is a hard link**  
*.*  

**What is the difference between a hard link and a symbolic link**  
*.*  

**What do the commands cp, mv, rm, mkdir do**  
*.*  

**What are wildcards and how do they work**  
*.*  

**How to use wildcards**  
*.*  

**Working With Commands**  
*.*  

**What do type, which, help, man commands do**  
*.*  

**What are the different kinds of commands**  
*.*  

**What is an alias**  
*.*  

**When do you use the command help instead of man**  
*.*  

**Reading Man Pages**  
*.*  

**How to read a man page**  
*.*  

**What are man page sections**  
*.*  

**What are the section numbers for User commands, System calls and Library functions**  
*.*  

**Keyboard shortcuts for Bash**  
*.*  

**Common shortcuts for Bash**  
*.*  

**LTS**  
*.*  

**What does LTS mean?**  
*.*  

**What does RTFM mean?**  
*.*  

**What is a Shebang**  
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
