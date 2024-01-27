#!/usr/bin/env python3
'''
By: Aliya Jordan
Date Started: 1/25/24

This file is for the client side of connected to a FTP server.
Has the features of a FTP application.
'''
import sys

def parse_arguments(command_arguments):
    '''
    This function parses the arguments from the command line 
    given by the user.
    @return: the arguments from the command line. 
    '''
    # Base case if no arguments passed into command line.
    if len(command_arguments) == 0:
        print("Please enter a command")
        sys.exit(1)
    # Case if the USER command is given.
    elif (command_arguments[0] == "USER"):
        # Check if actual username is given or not. 
        if (len(command_arguments) == 1):
            username = "anonymous"
        else:
            username = command_arguments[1]
        # Pass into USER command function
        user_command(username)
    # Case if the PASS command is given.
    elif (command_arguments[0] == "PASS"):
        # Check if actual password is given or not.
        if (len(command_arguments) == 1):
            password = None
        else:
            password = command_arguments[1]
        # Pass into PASS command function
        pass_command(password)
    # Case if TYPE I command is given.
    elif (command_arguments[0] == "TYPE"):
        if (len(command_arguments) == 1):
            print("Command not recognized")
            sys.exit(1)
        elif (command_arguments[1] == "I"):
            type_i_command()
    # Case if MODE S command is given. 
    elif (command_arguments[0] == "MODE"):
        if (len(command_arguments) == 1):
            print("Command not recognized")
            sys.exit(1)
        elif (command_arguments[1] == "S"):
            mode_s_command()
    # Case if STRU F command is given.
    elif (command_arguments[0] == "STRU"):
        if (len(command_arguments) == 1):
            print("Command not recognized")
            sys.exit(1)
        elif (command_arguments[1] == "F"):
            stru_f_command()
    # Case if LIST command is given.
    elif (command_arguments[0] == "LIST"):
        if (len(command_arguments) == 1):
            print("Need directory path")
            sys.exit(1)
        else:
            path = command_arguments[1]
            list_command(path)
    # Case if DELE command is given. 
    elif (command_arguments[0] == "DELE"):
        if (len(command_arguments) == 1):
            print("Need file path")
            sys.exit(1)
        else:
            path = command_arguments[1]
            dele_command(path)
    # Case if MKD command is given.
    elif (command_arguments[0] == "MKD"):
        if (len(command_arguments) == 1):
            print("Need directory path")
            sys.exit(1)
        else:
            path = command_arguments[1]
            mkd_command(path)
    # Case if RMD command is given.
    elif (command_arguments[0] == "RMD"):
        if (len(command_arguments) == 1):
            print("Need directory path")
            sys.exit(1)
        else:
            path = command_arguments[1]
            rmd_command(path)
    # Case if STOR command is given.
    elif (command_arguments[0] == "STOR"):
        if (len(command_arguments) == 1):
            print("Need file path")
            sys.exit(1)
        else:
            path = command_arguments[1]
            stor_command(path)
    # Case if RETR command is given.
    elif (command_arguments[0] == "RETR"):
        if (len(command_arguments) == 1):
            print("Need file path")
            sys.exit(1)
        else:
            path = command_arguments[1]
            retr_command(path)
    # Case if QUIT command is given.
    elif (command_arguments[0] == "QUIT"):
        quit_command()
    # Case if PASV command is given.
    elif (command_arguments[0] == "PASV"):
        pasv_command()
        
def user_command(username):
    '''
    This function is to incorporate the functionality of the USER command.
    @param username: the username of the user.
    '''
    print(username)

def pass_command(password):
    '''
    This function is to incorporate the functionality of the PASS command.
    @param password: the password of the user.
    '''
    print(password)

def type_i_command():
    '''
    This function is to incorporate the functionality of the TYPE I command.
    '''

def mode_s_command():
    '''
    This function is to incorporate the functionality of the MODE S command.
    '''

def stru_f_command():
    '''
    This function is to incorporate the functionality of the STRU F command.
    '''

def list_command(path):
    '''
    This function is to incorporate the functionality of the LIST command.
    @param path: the path of the directory where want contents listed.
    '''

def dele_command(path):
    '''
    This function is to incorporate the functionality of the DELE command.
    @param path: the path of the file want to delete.
    '''

def mkd_command(path):
    '''
    This function is to incorporate the functionality of the MKD command.
    @param path: the path of the directory want to make.
    '''

def rmd_command(path):
    '''
    This function is to incorporate the functionality of the RMD command.
    @param path: the path of the directory want to remove.
    '''

def stor_command(path):
    '''
    This function is to incorporate the functionality of the STOR command.
    @param path: the path of the file want to upload.
    '''

def retr_command(path):
    '''
    This function is to incorporate the functionality of the RETR command.
    @param path: the path of the file want to download. 
    '''

def quit_command():
    '''
    This function is to incorporate the functionality of the QUIT command.
    '''

def pasv_command():
    '''
    This function is to incorporate the functionality of the PASV command.
    '''





def main():
    '''
    This function is the main function of the client program.
    '''
    # Parse the arguments from the command line
    command_arguments = []
    for i in sys.argv[1:]:
        command_arguments.append(i)
    parse_arguments(command_arguments)


    

if __name__ == "__main__":
    main()