#!/usr/bin/env python3

import argparse
import socket

DEFAULT_SERVER = "proj5.3700.network"
DEFAULT_PORT = 443
# c38588ff3462a772700475eff5a7c03316eeba212be42c66795d767d25f55d43
class Crawler:
    '''
    This class is responsible for crawling the Fakebook server.
    '''
    def __init__(self, args):
        '''
        This is the constructor for the Crawler class. 
        It initializes the server, port, username, and password.
        Params:
            args: The arguments passed in from the command line.
        '''
        # Initialize the server, port, username, and password
        self.server = args.server
        self.port = args.port
        self.username = args.username
        self.password = args.password

    def run(self):
        # Send a request to the server
        request = "GET / HTTP/1.0\r\n\r\n"
        # Requesting the server to login
        print("Request to %s:%d" % (self.server, self.port))
        print(request)
        # Connect to the server
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((self.server, self.port))
        # Send the request, encode it to ascii
        mysocket.send(request.encode('ascii'))
        # Receive the response from the server
        data = mysocket.recv(1000)
        # Print the response, decode it to ascii
        print("Response:\n%s" % data.decode('ascii'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='crawl Fakebook')
    parser.add_argument('-s', dest="server", type=str, default=DEFAULT_SERVER, help="The server to crawl")
    parser.add_argument('-p', dest="port", type=int, default=DEFAULT_PORT, help="The port to use")
    parser.add_argument('username', type=str, help="The username to use")
    parser.add_argument('password', type=str, help="The password to use")
    args = parser.parse_args()
    sender = Crawler(args)
    sender.run()