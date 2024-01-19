'''
Made by: Aliya Jordan
Date: 1/17/2024

Project 1: This project is to implement a client program that plays a variant
of the recently popularized game Wordle. 
It makes guesses for the secret word, and will wait for the given server
to give information about how close your guess is. 
Once the client guesses the correct word, the server will return a secret flag that is unique to each student.

This client program support TLS encrypted sockets
'''
# Importing appropriate libraries
import argparse
import json
import socket 
import random

'''
This function parses the command line arguments. 
@Returns the parsed arguments
'''
def parse_args() :
    # create a parser object
    parser = argparse.ArgumentParser(description='Command Parser for Client Program')

    # add arguments to the parser object
    parser.add_argument('-p', type=int, help= "Port Number", required=False)
    parser.add_argument('-s', type=str, help= "Server Name", required=False)
    parser.add_argument('HostName', type=str, help= "Host Name" )
    parser.add_argument('NortheasternUsername', type=str, help= "Northeastern Username")

    return parser.parse_args()


'''
This function is able to connect to the server with parsed argument from the command line.
Once connected, will send hello message server to initiate protocol for the game.

@c_socket is the socket object
@HostName is the host name of the server
@p is the port number
@NortheasternUsername is the Northeastern Username
'''
def connect_to_server(c_socket, HostName, p, NortheasternUsername):
    c_socket.connect((HostName, p))

    # Send hello message to server
    hello_message = json.dumps({
        "type": "hello",
        "northeastern_username": NortheasternUsername
    }) + "\n"

    c_socket.send(hello_message.encode())

'''
This function reads the response from the server.
For debugging purposes.
@c_socket is the socket object
@Returns the response from the server 
'''
def read_response(c_socket):
    try:
        # Read response from server
        response = c_socket.recv(5000).decode()

        # Parse response from server
        response = json.loads(response)

        # If there is no response from the server.
        if response == None:
            print("There is no response from the server.")
            exit(1)

        # If there is a response, return it.
        return response
    
    #Error handling
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


'''
This function reads the wordlist.txt file and returns a list of words.
@Returns a list of words from the text file
'''
def read_wordlist():
    # Select the wordlist.txt file that is in the directory of Project 1.
    path = r"Project 1\wordlist.txt"
    # Read the file and send the guess to the server
    try:
        with open(path, "r") as file:
            contents = file.read()
            guesses = contents.split()
            return guesses
    # If file not found, print error File Not Found. 
    except FileNotFoundError:
        print(f"File not found")
        exit()
    # For any other error, print the error. 
    except Exception as e:
        print(f"Error: {e}")
        exit()

'''
This functions sends a guess to the server from the socket.
@c_socket is the socket object
@id is the id of the client for the current game
@guess is the word that is being guessed
'''
def send_a_guess(c_socket, id, guess):
    # Send guess message to server
    guess_message = json.dumps({
        "type": "guess",
        "id": id,
        "word": guess
    }) + "\n"
    c_socket.send(guess_message.encode())

'''
This function fiters the list of filtered_words
'''
def filter_words(guesses, guessed_words, marks_list):
    filtered_list = []

    # iterate through the words in the whole entire guesses list
    for word in guesses:
        # set variable checker to true
        is_valid = True

        # iterate through the guessed words and the corresponding marks list
        for guessed_word, marks in zip(guessed_words, marks_list):
            # iterate through the letters in the guessed word and the corresponding marks array
            for letter, mark in zip(guessed_word, marks):
                # if the mark is 0 and the letter is in the word, then not valid letter
                if mark == 0 and letter in word:
                    is_valid = False
                    break
                # if the mark is 1 and the letter is not in the word, then not valid letter
                elif mark == 1 and letter not in word:
                    is_valid = False
                    break
                elif mark == 2:
                    if letter != word[guessed_word.index(letter)]:
                        is_valid = False
                        break

        if is_valid:
            filtered_list.append(word)

    return filtered_list

'''
This is a main function that runs the program.
'''
def main():
    # Parse the command line arguments
    args = parse_args()
    # Create a stream socket object
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    connect_to_server(c_socket, HostName=args.HostName, p=args.p, NortheasternUsername=args.NortheasternUsername)
    id = read_response(c_socket)["id"]

    # Perform guess
    guesses = read_wordlist()
    guess = random.choice(guesses)
    send_a_guess(c_socket, id, guess)

    while True:
        # Receive response
        response = read_response(c_socket)

        if response["type"] == "bye":
            print("Yay you got it!: " + response["flag"])
            break
        elif response["type"] == "retry":
            guessed_words = [guess["word"] for guess in response["guesses"]]
            marks_list = [mark["marks"] for mark in response["guesses"]]
            # Filter words based on response
            filtered_list = filter_words(guesses, guessed_words, marks_list)

            if len(filtered_list) == 0:
                print("No words left to guess")
                exit(1)
            else:
                 # Send guess
                guess = random.choice(filtered_list)
                send_a_guess(c_socket, id, guess)
        else:
            print("Invalid response from server")
            exit(1)

        
if __name__ == "__main__":
    main()
