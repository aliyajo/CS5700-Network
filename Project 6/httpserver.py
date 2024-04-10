from http.server import *
import argparse
import json
import os
import psutil
import requests
import socket
import urllib.request


'''
Implementation notes:

basic implementation -- act as a proxy(pass thru), when request comes in, fetch/download content from origin server and send it back to client
    - my port range: 20380-20389

    - ssh into the http server
        `ssh -i ssh-ed25519-quach.l.priv quach.l@cdn-http3.khoury.northeastern.edu`
        `ssh -i ssh-ed25519-quach.l.priv quach.l@cdn-http4.khoury.northeastern.edu`
        
    - upload the httpserver.py file to the server
        `scp -i ssh/ssh-ed25519-quach.l.priv httpserver.py quach.l@cdn-http3.khoury.northeastern.edu:~/`
        `scp -i ssh/ssh-ed25519-quach.l.priv httpserver.py quach.l@cdn-http4.khoury.northeastern.edu:~/`
        `scp -i ssh/ssh-ed25519-quach.l.priv httpserver.py quach.l@cdn-http7.khoury.northeastern.edu:~/`
        
        
    - run http server
        `python3 httpserver.py -p 20380 -o cs5700cdnorigin.ccs.neu.edu`
        
    - curl command to test the HTTP server
        curl http://cs5700cdnorigin.ccs.neu.edu:8080
        curl http://cs5700cdnorigin.ccs.neu.edu:8080/Ariana_Grande

    - check if server is running
        `time wget http://45.33.55.171:20380/cs5700cdn.example.com`?????
        `time wget http://cdn-http3.khoury.northeastern.edu:20380/cs5700cdn.example.com
        `time wget http://cdn-http4.khoury.northeastern.edu:20380/cs5700cdnorigin.ccs.neu.edu:8080/Ariana_Grande

'''

ORIGIN_SERVER = 'cs5700cdnorigin.ccs.neu.edu' 
ORIGIN_SERVER_PORT = 8080

# basic implementation of proxy server (pass thru)
class HTTPRequestHandler(BaseHTTPRequestHandler):
    cache = {}

    def do_GET(self):
        '''
        Handles GET requests, fetches data from origin server & sends it back to client.
        '''
        # for path `/grading/beacon` return 204 status code
        if self.path == '/grading/beacon':
            self.send_response(204)
            self.end_headers()
            return
        elif self.path == '/get_server_info':
            cpu_percent = psutil.cpu_percent()
            memory_info = psutil.virtual_memory()
            load_avg = os.getloadavg()

            server_info = {
                'cpu_percent': cpu_percent,
                'memory_used_percent': memory_info.percent,
                'memory_total': memory_info.total,
                'load_average': load_avg,
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(server_info).encode())  # Convert server_info to JSON string
            return

        cache_content = self.cache.get(self.path)
        if cache_content:
            # send response status code
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # send cached response data/content to client
            self.wfile.write(cache_content)
            return
        else:
            # fetch data from origin server
            try:
                with urllib.request.urlopen(f'http://{ORIGIN_SERVER}:{ORIGIN_SERVER_PORT}{self.path}') as response:
                    content = response.read()
                    self.cache[self.path] = content
                    self.send_response(response.getcode())
                    self.send_header('Content-type', response.info()['Content-type'])
                    self.end_headers()
                    self.wfile.write(content)

            except urllib.error.HTTPError as e:
                self.send_error(e.code, e.reason)
            except urllib.error.URLError as e:
                self.send_error(502, 'Failed to fetch data from origin server')
            except Exception as e:
                self.send_error(500, 'Internal server error')
                print(f' ** ERROR: {e} ** ')
            return


def run_http_server(port, origin_server):
    '''
    Runs the HTTP server.
    '''
    # set origin server url for handler class
    HTTPRequestHandler.origin_server = origin_server
    server_address = ('', port)

    # create server socket
    http_server = HTTPServer(server_address, HTTPRequestHandler)
    print(f' ** http server running on port {port} ** ')
    http_server.serve_forever()


def parse_args():
    '''
    Parses command line arguments.
    '''
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('-p', '--port', required=True, type=int, help='Port number to bind HTTP server to')
    parser.add_argument('-o', '--origin', required=True, type=str, help='Name of origin server for CDN')
    return parser.parse_args()


def main():
    args = parse_args()
    run_http_server(args.port, args.origin)


if __name__ == '__main__':
    main()