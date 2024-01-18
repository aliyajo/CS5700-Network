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
# Import argsparse for dealing with command prompt
import argparse
import json
import socket 
import json

'''
This function parses the command line arguments. 
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
'''
def connect_to_server(c_socket, HostName, p, NortheasternUsername):
    c_socket.connect((HostName, p))

    # Send hello message to server
    hello_message = json.dumps({
        "type": "hello",
        "northeastern_username": NortheasternUsername
    }) + "\n"

    c_socket.send(hello_message.encode())

def guess():

def send_guess(c_socket, guess):
    # Send guess message to server
    guess_message = json.dumps({
        "type": "guess",
        "guess": guess
    }) + "\n"

    c_socket.send(guess_message.encode())

def read_response(c_socket):
    # Read response from server
    response = c_socket.recv(4096).decode()

    # Parse response from server
    response = json.loads(response)

    return response

def main():
    # Parse the command line arguments
    args = parse_args()

    # Create a stream socket object
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    connect_to_server(c_socket, HostName=args.HostName, p=args.p, NortheasternUsername=args.NortheasternUsername)
    print(read_response(c_socket)) 
    # Send guess to server
    guess = guess()
    send_guess(c_socket, guess)
    print(read_response(c_socket))
if __name__ == "__main__":
    main()
