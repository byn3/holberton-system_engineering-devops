# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---

**Linux file permissions**  
*Yup. Learned a lot of them.*  

**What do the commands chmod, sudo, su, chown, chgrp do?**  
*chmod - changes mode like change user or groups permissions. sudo is a one time use of su and asks and does 1 super user command. su is when you become a superuser (this is very dangerous if you don't kow your stuff). chown is change ownership. chgrp is change group.*  

**How to represent each of the three sets of permissions (owner, group, and other) as a single digit?**  
*7 is rwx all. 6 is rw- all. 5 is r-x a. 4 is r-- ugo. 3 is -wx all. 2 is -w- ugo. 1 is --x for all. 0 is no permissions, ---.*  

**How to change permissions, owner and group of a file?**  
*chmod, chown, chgrp. Examples are chmod u+x \<FILENAME> and that gives the user/ owner of the file execute permissions. chown bryan:holberton danceWithTheDead will change the danceWithTheDead file owner to bryan and the group to holberton. chgrp monkeyDLuffy Jinbei will change the file Jinbei to the monkeyDLuffy group (or the Straw Hats).*  

**Why can’t a normal user chown a file?**  
*Because bad things can happen. The user can give away important files which is very bad. Only the root or su should have that power. But no one man should have all that power.*  

**How to run a command with root privileges?**  
*su or sudo. su will promt you to enter root password and sudo will promt you to enter your own password.*  

**How to change user ID or become superuser?**  
*su to become super user, usermod -u NEWuserID OLDuserID. u flag is UID and l flag is loginUserName. And example is usermod -l Caitlyn Bruce.*  

**How to create a user?**  
*"sudo useradd USERNAME" should work. Adding a -m flag will create a home dir if it does not exist.*  

**How to create a group?**  
*sudo groupadd eliteTen. That should create a new eliteTen group who can take down Azami. Or sudo groupadd Avengers and that should stop Loki and Ultron but oh man Thanos. He curb stomped their faces.*  

**How to print real and effective user and group IDs?**  
*id prints them out. Adding the flags -g shows effective group, -G for all group IDs, -r for real ID, -n for name instead of number, -u for effective user ID.*  

**How to print the groups a user is in?**  
*id -G.*  

**How to print the effective userid?**  
*id -u.*  

## Each scripts and their output  
*Script 0 - Create a script that changes your user ID to betty.  
*Script 1 - Write a script that prints the effective userid of the current user.  
*Script 2 - Write a script that prints all the groups the current user is part of.  
*Script 3 - Write a script that changes the owner of the file hello to the user betty.  
*Script 4 - Write a script that creates an empty file called hello.  
*Script 5 - Write a script that adds execute permission to the owner of the file hello.  
*Script 6 - Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.  
*Script 7 - Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello.  
*Script 8 - Write a script that sets the permission to the file hello as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permissions.  
*Script 9 - Write a script that sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.  
*Script 10 - Write a script that sets the mode of the file hello the same as olleh’s mode. The file hello will be in the working directory. The file olleh will be in the working directory.  
*Script 11 - Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.  
*Script 12 - Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.  
*Script 13 - Write a script that changes the group owner to holberton for the file hello. The file hello will be in the working directory.  
*Script 14 - Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.  
*Script 15 - Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively. The file _hello is in the working directory. The file _hello is a symbolic link.  
*Script 16 - Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume. The file hello will be in the working directory.  
*Script 100 - Write a script that will play the StarWars IV episode in the terminal.  
*Script 101 - Create a man that looks exactly like this one and passes all checks. NOTE: A new line is not necessary at the end of this file, refer to the output of wc, as shown below.  


#### Limitation of these projects:  
___
-Allowed editors: vi, vim, emacs  
-All your scripts will be tested on Ubuntu 14.04 LTS  
-All your scripts should be exactly two lines long ($ wc -l file should print 2)  
-All your files should end with a new line (why?)  
-The first line of all your files should be exactly #!/bin/bash  
-A README.md file, at the root of the folder of the project, describing what each script is doing  
-You are not allowed to use backticks, &&, || or ;  
-All your files must be executable  
