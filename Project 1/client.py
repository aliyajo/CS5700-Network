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
def connect_to_server(HostName, p):
    # Create a stream socket object
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.connect((HostName, p))

    # Send hello message to server
    hello_message = '{"type": "hello", "northeastern_username": "<your-My.Northeastern-username>"}\n'
    socket.sendall(hello_message.encode())    

    
def main():
    # Parse the command line arguments
    args = parse_args()

    # Connect to the server
    connect_to_server(HostName=args.HostName, p=args.p)

if __name__ == "__main__":
    main()
