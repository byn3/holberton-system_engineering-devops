What is a server
A computer that does a lot of services.





Where server usually live
Data centers.




What is SSH
Secure SHell.




How to create an SSH RSA key pair
ssh-keygen





How to connect to a remote host using an SSH RSA key pair
ssh remote\_host
ssh username@remote\_host












Server (computing)
A purpose of a server is to share data and resources and distribute work. A lot
of the internet is based off of a client-server model and many actions requires
more than one server. Hard drive, CPU, and memoery space are huge hardware
wise. A server's OS is specifically designed to provide different services.

Lots of different services and servers.

SSH is main way to connect to Linux servers remotely and securly. All commands
in the terminal are sent to the remote server and executed there. When I log in
through SSH, I use an account that exists on the remote server. I enter a
shell session which is an encrypted tunnel. To establish the SSH connection,
the remote machine needs to run an SSH daemon. That sooftware listens for
connections to a specific port and authenticates the requests and creates the
sessions.

Passwords are not secure. SSH keys are very secure. SSH keys have a public and
private key. Public can be shared without concern and private must be super
secret. For authentication with SSH keys, a user must have the key pair on
their computer and the remote server needs the public copy within the user's
home dir. (~/.ssh/authorized\_keys). This file contains a list of public keys,
one each line and all those keys are authorized to go into the account.

SSH key authentication infiorms server of the intent and which public key to
use. The server checks the authorized\_keys file for the public key files. It
generated a random string and encrypts it which the private key decrypts.
Server sends the string to client to test if their private key is right.

MD5 hash is transmitted back to server after the client did magic. To make a
new SSH key pair type in ssh-keygen. SSH keys are 2048 bits and it can be
increased with the flag -b and a bigger number of bits like -b 4096. 


SO MUCH READING
https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys


