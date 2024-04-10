#!/usr/bin/env python3
import argparse
import http.server
import socket


class HTTPServer(http.server.BaseHTTPRequestHandler):
    '''
    This class is the HTTP server.
    '''
    def __init__ (self, args):
        '''
        This is the constructor for the HTTPServer class.
        '''
        self.port = args.port
        self.origin = args.origin

    def handle_GET(self):
        '''
        This function is responsible for handling the GET request.
        '''
        pass

    def handle_PERFORMANCE_METRICS(self):
        '''
        This function is responsible for handling the PERFORMANCE_METRICS request.
        '''
        self.write("APPLE PERFORMANCE_METRICS")


    
    def run(self):
        '''
        This is the main function for running the HTTP server
        '''
        try:
            server = http.server.HTTPServer(('', self.port), self)
            print('Started http server')
            server.serve_forever()
        except Exception as e:
            print(e)
        
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Server')
    # Parse for the port number
    parser.add_argument('-p', '--port', type=int, required=True,  help='Port number to listen on')
    parser.add_argument('-o', '--origin', type=str, required=True, help='Origin server')
    args = parser.parse_args()
    # Create the server
    server = HTTPServer(args)
    # Run the server
    server.run()