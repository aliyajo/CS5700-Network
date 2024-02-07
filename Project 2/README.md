Project 2: FTP Client
By: Aliya Jordan

## Overview 
    This python file is for the client side of connecting to a FTP server.
    It has features of a FTP application: uploading information to the server, downloading information to the server, making a new directory, removing a directory, removing a file, and moving file around.

## Features
    Able to efficiently connect to a FTP server and communicate in a way to move around files. 

## Command Line Arguments
    ls <URL> 
        'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
    mkdir <URL>    
        'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH         
    rm <URL> 
        'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
    rmdir <URL> 
        'URL': Has the format of : ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
    cp <ARG1> <ARG2>
        If copying from local machine to a FTP server:
            'ARG1': Local directory path
            'ARG2': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
        If copying from FTP server to the local machine:
            'ARG1': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
            'ARG2': Local directory path
    mv <ARG1> <ARG2>
        If moving from local machine to a FTP server:
            'ARG1': Local directory path
            'ARG2': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
        If moving from FTP server to the local machine:
            'ARG1': FTP server URL which has the format: ftp://[USER[:PASSWORD]@]HOST[:PORT]/PATH
            'ARG2': Local directory path

## Functions

**parse_arguments():
    This function parses the arguments from the command line.
    Returns the parsed arguments

**parse_URL(url):
    This function parses the URL given by the user
    Params:
        @url: The URL given by the user
    Returns the username, password, host, port number, and server_path of the URL.

**print_server_message(control_socket):
    This function prints the message from the server. 
    Params:
        @control_socket: The control channel socket object. 

**connect_to_server(host, port, username, password)
    This function connects tot he server with the given host and port number. 
    Params:
        @Host: The host name of the server
        @Port: The port number of the server
        @Username: The username of the server
        @Password: The password of the server
    Returns the control channel socket object

**connect_to_data_channel(control_socket):
    This function connects to the data channel of the server. 
    Params:
        @control_socket: The control channel socket object
    Returns the data channel socket object. 

**ls_command(control_socket, server_path):
    This function is able to efficiently communication between server and client for the ls command.
    -- It uses the data channel socket, but will not close it since the server is sending data over -- 
    Params:
        @control_socket: The control channel socket object
        @server_path: The path to the directory on the server

**rm_command(control_socket, server_path):
    This function performs efficient communication between the server and client for the rm command. 
    Params:
        @control_socket: The control channel socket object
        @server_path: The path to the directory on the server

**mkdir_command(control_socket, server_path):
    This functions performs efficient communication between the server and client for the mkdir command. 
    Params:
        @control_socket: The control channel socket object.
        @server_path: The path to the directory on the server. 

**rmdir_command(control_socket, server_path):
    This function performs efficient communication between the server and client for the rmdir command
    Params:
        @control_socket: The control channel socket object
        @server_path: The path to the directory on the server

**cp_command_from_server(control_socket, local_machine_path, server_path):
    This function performs efficient communication between the server and client for the cp command-- downloading file from the server.
    -- Using data channel socket, will not close data channel since the server is sending the data -- 
    Params:
        @control_socket: The control channel socket object
        @local_machine_path: The path on the local machine
        @server_path: The path to the directory on the server

**cp_command(control_socket, local_machine_path, server_path, download):
    This function performs efficient communication between the server and client for the cp command-- downloading file to the server.
    -- Using data channel socket, will close data channel since the local machine is sending the data -- 
    Params:
        @control_socket: The control channel socket object
        @local_machine_path: The path on the local machine
        @server_path: The path to the directory on the server
        @download: A boolean indicating whether to download or upload the file.

**mv_command(control_socket, local_machine_path, server_path, download):
    This function performs efficient communication between the server and client for the cp command-- downloading file to the server.
    -- Using data channel socket, will close data channel since the local machine is sending the data -- 
    Params:
        @control_socket: The control channel socket object
        @local_machine_path: The path on the local machine
        @server_path: The path to the directory on the server
        @upload: A boolean indicating whether to download or upload the file.

**main():
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