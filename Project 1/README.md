By: Aliya Jordan


## Overview
This Python file is able to successfully communicate to the given server that is inputted on the command line. This communication involves back-and-forth messages that help the client play Wordle, and determine if successfully guess the word if server returns the secret flag. 

## Features
Able to connect to either TLS connections, or TLS encrytpted connections. 

## Command Line Arguments
<-p port> <-s> < hostname > < Northeastern-username >

'-p': Port number (optional)
'-s': TLS encrypted socket connection (optional)
'hostname': Name of the server (required)
'Northeastern-username': Northeastern username without the email context (required)

## Functions

**parse_args(): 
    This function parses the command line arguments
    Returns the parsed arguments so it can be used to accurately run the game
**connect_to_server(HostName, p, s, NortheasternUsername):
    This function allows the connection to the server with the parsed argument. Once connected, it will send a "hello" message to server in JSON format to initiate protocol for the game.
    Params:
        @HostName is the host name of the server
        @p is the port number
        @NortheasternUsername is the Northeastern Username
    Returns socket object
**read_response(c_socket):
    This function allows us to read the response from the server
    Params:
        @c_socket is the socket object
    Returns the response from the server 
**read_wordlist():
    This functions allows us to read the given official Wordle word list.
    Returns list of words from the text file
**send_a_guess(c_socket, id, guess):
    This function allows us to send a guessed word to the server from the socket. 
    Params:
        @c_socket is the socket object
        @id is the id of the client for the current game
        @guess is the word that is being guessed
**filter_word(guesses, guessed_word, marks):
    This function filters the guesses list based on the current guessed word, and its corresponding marks. 
    (Function that implements marks to determine the Wordle word)
    Params:
        @guesses is the list of official words used by Wordle. 
        @guessed_word is the word that was guessed for the current iteration.
        @marks is the list of marks that correspond to the guessed word.
    Returns: a list of filtered words from the guesses list. 
**main():
    This is the main function that runs the entire game.

## Approach Taken
    For this project, I wanted to implement that marks that the server gave back instead of a brute-forced approach. 
    This approach involved also using the message type "retry" from the server to determine the history of words, and their corresponding marks. 

    Based off of this, it used the last guessed word, and its corresponding marks, and iterates through them to determine's each individual letter's relationship with the Wordle word. 

    This is iterated alongside each word in the official word list, and compares each letter that has been marked in the iteration with the word being seen in the official word list.This is appended to the filtered list, and a random choice from this list is given to the server. If the word is correct, then will be given the secret flag. If the word is not correct, this process is redone.  

    Some challenges that happened was before coming up with this final solution, I just used the entire history of guessed words, with their corresponding marks. In this, it would iterate through this array of marks with the corresponding list of guessed word every time the game was ran. This resulted in the returned filtered_list to be ran out of words before the game could be solved. 

    Once realizing the game was deleting words that weren't needing to be iterated, this is when the decision to use the current guessed word in the iteration then the whole entire list. 

    I also made sure when reviewing mark 0, that the letter in the current guessed word is present in the current official word, or the letter is not in the current position, but is still in the word, then the word is not valid. 

    My overall challenge was mass deletion from the program, and with this fix, it solved it. :)

## Testing
    Testing was done through print statements during the debugging process of the code. This allowed me to determine the before challenge of mass deletion due to the print statement. 

    Print statements also let me be able to ensure the marks filter are correctly filtering. 



