Project 1: Socket Basics

By: Aliya Jordan

## Overview
This Python file is able to successfully communicate to the given server that is inputted on the command line. This communication involves back-and-forth messages that help the client play Wordle, and determine if successfully guess the word if server returns the secret flag. 


In order to run the program proficiently, the wordlist.txt file must be downloaded alongside the client.py file. It must be in the same directory as the client file due the file utilizing it for the official word list of Wordle. 

## Features
Able to connect to either TLS connections, or TLS encrytpted connections. 

## Command Line Arguments
    <-p port> <-s> < hostname > < Northeastern-username >
    '-p': Port number (optional)
    '-s': TLS encrypted socket connection (optional)
    'hostname': Name of the server (required)
    'Northeastern-username': Northeastern username without the email context (required)

## Functions
To log in, will need to give correct parameters to the following function: 
- connect_to_server(HostName, p, s, NortheasternUsername):

  This function allows the connection to the server with the parsed argument. Once connected, it will send a "hello" message to server in JSON format to initiate protocol for the game.
  
    Params:
        @HostName is the host name of the server
        @p is the port number
        @NortheasternUsername is the Northeastern Username
  
    Returns socket object

This is the main function needed to be ran in order to use. 
- main():

    This is the main function that runs the entire game.

## Modules Used
For this code, some built-in python modules that were imported in order to make the code functional when accomplishing the overall goal of the program. 
- argparse: module that allows easy user-friendly command-line interfaces

- json: module that ensures JSON format is being used for communication between client and server. This is needed since the server only recieves JSON formatted messages, and returns JSON formatted message. 

- socket: module that allows the usage of sockets within the code.

- random: module  that lets random selection from the given lists in the code. 

- ssl: module for TLS/SSL wrapper for socket objects. Needed to allow TLS encryption socket connection. 


## Approach Taken

For this project, I wanted to implement that marks that the server gave back instead of a brute-forced approach. 
This approach involved also using the message type "retry" from the server to determine the history of words, and their corresponding marks. 

Based off of this, it used the last guessed word, and its corresponding marks, and iterates through them to determine's each individual letter's relationship with the Wordle word. 

This is iterated alongside each word in the official word list, and compares each letter that has been marked in the iteration with the word being seen in the official word list.This is appended to the filtered list, and a random choice from this list is given to the server. If the word is correct, then will be given the secret flag. If the word is not correct, this process is redone.  

Some challenges that happened was before coming up with this final solution, I just used the entire history of guessed words, with their corresponding marks. In this, it would iterate through this array of marks with the corresponding list of guessed word every time the game was ran. This resulted in the returned filtered_list to be ran out of words before the game could be solved. 

Once realizing the game was deleting words that weren't needing to be iterated, this is when the decision to use the current guessed word in the iteration then the whole entire list of guessed words history. 

I also made sure when reviewing mark 0, that the letter in the current guessed word is present in the current official word, or the letter is not in the current position, but is still in the word, then the word is not valid. 

My overall challenge was mass deletion from the program, and with this fix of just using current word and its corresponding marks, it solved it. :)

## Testing
Testing was done through print statements during the debugging process of the code. This allowed me to determine the before challenge of mass deletion due to the print statement. 


Print statements also let me be able to ensure the marks filter are correctly filtering. 

## Resources Used
For this assignment, due to the implementation of connecting with sockets, there were some outside resources used in order to implement it correctly in my code: 

- https://docs.python.org/3.2/library/ssl.html
- https://docs.python.org/3/howto/sockets.html
- https://www.datacamp.com/tutorial
- https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python 
