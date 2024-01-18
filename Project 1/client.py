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

# create a parser object
parser = argparse.ArgumentParser(description='Command Parser for Client Program')

# add arguments to the parser object
parser.add_argument('-p', type=int, help= "Port Number", required=False)
args = parser.parse_args()
print(args)
parser.add_argument('-s', type=str, help= "Server Name", required=False)
parser.add_argument(type=str, help= "Host Name", required = True)
parser.add_argument(type=str, help = "Northeastern Username", required = True)


