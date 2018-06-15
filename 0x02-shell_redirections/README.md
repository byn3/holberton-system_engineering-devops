# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---

**What do the commands head, tail, find, wc, sort, uniq, grep, tr do?**  
*head outputs the first part of the files (default 10 lines). So “head -n99 beer wall” gives the first 99 lines from the files beer and wall. The -c flag will give back bits while -n is lines. tail is the same as head but for lines at end of file. find searches and locates lists of files and dir based on conditions I set. find <path> -name <filename> works and other flags will be useful like -f for type or -perm for permissions or -user for user or -group for group or -mtime # for days modified # of days back or -atime # for accessed # of days back or -cmin or -mmin and a whole bunch of other good flags. wc is word count. wc -lwcmL is for lines, words, bytes, chars, or length of longest line. sort sorts. sort will rearrange the lines in a .txt file so they are numerically and alphabetically sorted. Some rules are number before letters and lowercase before the uppercase (eg. a A b c C z). Lots of good flags for this one including ignoring blanks and merge files. uniq reports or filters out repeated lines in a file. Most popular flags outs probably be -cdu. grep is regex. I can type ‘grep “stringConstant filename.’ Lots of good flags for this like case insensitive search, recursive search, show which lines do not match, etc. tr is for translating, deleting or squeezing repeated chars. Very useful for replacement text by default. “tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ” will convert all to uppercase. [:lower:] and [:upper:] works too. So do a-z and A-Z.*  
  
**How to redirect standard output to a file?**  
*> will redirect output. 1> is default which is display stdout and 2> is stderr. cat > box.txt [INPUT] will overwrite INPUT into box. > will override and >> will append.*  

**How to get standard input from a file instead of the keyboard?**  
*< will work. So I can do “sort < gotei13.txt” and that should sort all the captains instead of me manually inputting all their names.*  

**How to send the output from one program to the input of another program?**  
*< and > will do the work. Need to change flags or other stuff depending on the goal. Also piping should work too, |. *  

**How to combine commands and filters with redirections?**  
*You just pipe or connect them with |, <, >. Logic.*  

**What are special characters?**  
*Characters that carry out a special instruction or have a different meaning than we intend them to, also known as meta-characters.*  

**Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them?**  
*Done. White space is to determine when things begin and end. Single quotes are string literals so special characters inside them are ignored. Double quotes prevent the text inside from being split into multiple but it does allow command line substitutions. Backslash prevents the next char from being interpreted as a special character. comment is # so \# wouldn’t be a comment. Pipe redirects output from an initial common to the input of a secondary command, used to chain commands together. Command separator is ;. It is common for IF THEN statement and it represents a newline. Tilde is ~. ~ is the home directory.*  

**How to display a line of text?**  
*We can use cat to display the file or cat -n to display the first to nth lines. Or we can use sed. sed -n 5p filename will print out line 5 of filename.*  

**How to concatenate files and print on the standard output?**  
*cat file1.txt file2.txt file3.txt…*  

**How to reverse a string?**  
*Examples include echo “STRING” | rev or rev<<<“STRING”. There are other ways too.*  

**How to remove sections from each line of files?**  
*cut. I am Bon Qui Qui and I will cut you. We can cut the nth byte, or character, or other ways with a lot of diff flags. I can use sed also to do some magic, maybe. *  

**What is the /etc/passwd file and what is its format?**  
*It has login info of users. 7 fields on each line, first is account name, second is placeholder for password info (obtained in etc/shadow), third is User ID and the root is always UID 0, 4th is group ID, 5th is comment field, 6th is home dir (usually /home/username since we ain’t root people), 7th is user shell like bin/bash. This field contains the shell that will be spawned.*  

**What is the /etc/shadow file and what is its format**  
*The passwords. Long ago passwords use to be hashed in the /passwd file but lots of people have read permissions there so dat hella bad. The keys are not stored in plain text or at least they shouldn’t be. This place should have key derivation functions to make a new hash. This file should be unreadable by unprivileged users. There is a shadow group and they have read permissions. 7 password fields and they are defined. First is daemon or account username. Second is salt and hashed password. 3rd is last password change date, measures in unix epoch time. 4th is the days until password change is permitted (0 means no restrictions). 5th is days until password change is required and 99999 means there is no limit. 6th is the days of warning prior to expiration (useful for password change requirement workplaces). 7th is kinda blankish sometimes. The last 3 fields denote days before the account was inactive, days since the Epoch when the account expires, and last field is unused.*  


## Each scripts and their output  
*Script 0 - Write a script that prints “Hello, World”, followed by a new line to the standard output.   
*Script 1 - Write a script that displays a confused smiley "(Ôo)'.  
*Script 2 - Display the content of the /etc/passwd file.  
*Script 3 - Display the content of /etc/passwd and /etc/hosts  
*Script 4 - Display the last 10 lines of /etc/passwd  
*Script 5 - Display the first 10 lines of /etc/passwd  
*Script 6 - Write a script that displays the third line of the file iacta. The file iacta will be in the working directory. You’re not allowed to use sed.  
*Script 7 - Write a shell script that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.   
*Script 8 - Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.   
*Script 9 - Write a script that duplicates the last line of the file iacta. The file iacta will be in the working directory  
*Script 10 - Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.   
*Script 11 - Write a script that counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted.  
*Script 12 - Create a script that displays the 10 newest files in the current directory.  
*Script 13 - Create a script that takes a list of words as input and prints only words that appear exactly once. Input   format: One line, one word. Output format: One line, one word. Words should be sorted   
*Script 14 - Display lines containing the pattern “root” from the file /etc/passwd  
*Script 15 - Display the number of lines that contain the pattern “bin” in the file /etc/passwd  
*Script 16 - Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.  
*Script 17 - Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.  
*Script 18 - Display all lines of the file /etc/ssh/sshd_config starting with a letter.  
*Script 19 - Replace all characters A and c from input to Z and e respectively.  
*Script 20 - Create a script that removes all letters c and C from input.  
*Script 21 - Write a script that reverse its input.  
*Script 22 - Write a script that displays all users and their home directories, sorted by users. Based on the the /etc/passwd file.   
*Script 100 - Write a command that finds all empty files and directories in the current directory and all sub-directories. Only the names of the files and directories should be displayed (not the entire path). Hidden files should be listed. One file name per line. The listing should end with a new line. You are not allowed to use basename, grep, egrep, fgrep or rgrep  
*Script 101 - Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories. Hidden files should be listed. Only regular files (not directories) should be listed. The names of the files should be displayed without their extensions. The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay). One file name per line. The listing should end with a new line. You are not allowed to use basename, grep, egrep, fgrep or rgrep.  
*Script 102 - An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more. Create a script that decodes acrostics that use the first letter of each line. The ‘decoded’ message has to end with a new line. You are not allowed to use grep, egrep, fgrep or rgrep.  
*Script 103 - Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests. Order by number of requests, most active host or IP at the top. You are not allowed to use grep, egrep, fgrep or rgrep.  


#### Limitation of these proects:  
___
-Allowed editors: vi, vim, emacs
-All your scripts will be tested on Ubuntu 14.04 LTS
-All your scripts should be exactly two lines long ($ wc -l file should print 2)
-All your files should end with a new line (why?)
-The first line of all your files should be exactly #!/bin/bash
-A README.md file, at the root of the folder of the project, describing what each script is doing
-You are not allowed to use backticks, &&, || or ;
-All your files must be executable
-You are not allowed to use sed or awk
