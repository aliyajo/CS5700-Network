Project 2: FTP Client

By: Aliya Jordan

## Overview 
This python file is for the client side of connecting to a FTP server.
It has features of a FTP application: uploading information to the server, downloading information to the server, making a new directory, removing a directory, removing a file, and moving file around.

## Features
Able to efficiently connect to a FTP server and communicate in a way to move around files. 

## Command Line Arguments
- ls $<$ URL $>$

      'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
- mkdir $<$ URL $>$

      'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH         
- rm $<$ URL $>$

      'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
- rmdir $<$ URL $>$

      'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
- cp $<$ ARG1 $>$ $<$ ARG2 $>$

      If copying from local machine to a FTP server:
            'ARG1': Local directory path
            'ARG2': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
        If copying from FTP server to the local machine:
            'ARG1': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
            'ARG2': Local directory path
- mv $<$ ARG1 $>$ $<$ ARG2 $>$

      If moving from local machine to a FTP server:
            'ARG1': Local directory path
            'ARG2': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
        If moving from FTP server to the local machine:
            'ARG1': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
            'ARG2': Local directory path
## Functions:
- main():
    This is the main function that runs this FTP client program.
  
## Modules used:
For this code, some built-in python modules that were imported in order to make the code functional when accomplishing the overall goal of the program. 
- argparse: module that allows easy user-friendly command-line interfaces.
- socket: module that allows the usage of sockets within the code.
- urlparse: module that parse the url.

## Approach Taken:
    
For this project, implemented the basic functions of a FTP client to the FTP server. 


It parses the commands given in the command line. From here it parses the Url and retrieves the Username, Password, Port, and Host Name to connect to the FTP server. 


One thing consistent throughout the code is the usage of the control_socket. This is the main communication socket with the FTP client (this program) and the FTP server. Here we can figure out debugging processes, and if the command was executed well.


There is a usage of the data channel socket within the cp_command() and mv_command() function. This is because it involves the uploading and downloading of data across the server and client and vice-versa. Here we esablish a data channel socket that is able to communicate data from the server and to the server. All the rest of the functions are not involving the data channel. 


The data channel is established by asking the server the parameters to connect the socket to the server. This is done by parsing this given message, and computing the correct port number and IP address number. 


There was no crazy implementation, just the basics to make sure the FTP client efficiently communicated with the FTP server.


The challenges in this was mainly incorporating the data channel efficiently. I was having issue on this, but was able to solve it through the debugging process of using print statements. 

## Testing
Testing was done through print statements during the debugging process of the code. It let me deciver what the server was saying it was recieving data/sending data.

## Resources used
- https://docs.python.org/3/library/argparse.html 
- https://docs.python.org/3/library/urllib.parse.html
- https://www.tutorialspoint.com/What-does-the-b-modifier-do-when-a-file-is-opened-using-Python 
