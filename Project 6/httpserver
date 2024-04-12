#!/usr/bin/env python3
from http.server import *
import argparse
import json
import os
import psutil
import urllib.request
from collections import OrderedDict
import zlib

ORIGIN_SERVER = 'cs5700cdnorigin.ccs.neu.edu' 
ORIGIN_SERVER_PORT = 8080


class HTTPRequestHandler(BaseHTTPRequestHandler):
    '''
    HTTP request handler class.
    '''
    # ordered dictionary to store cache content in LRU order
    cache = OrderedDict()
    cache_size = 20


    def do_GET(self):
        '''
        Handles GET requests, fetches data from origin server & sends it back to client.
        '''
        # for path `/grading/beacon` return 204 status code
        if self.path == '/grading/beacon':
            self.send_response(204)
            self.end_headers()
            return

        # check if path is in cache
        if self.path in self.cache:
            content, content_type, status_code = self.cache[self.path]
            self.send_content(content, content_type, from_cache=True, status_code=status_code)
            return
        
        # fetch data from origin server
        else: 
            try:
                with urllib.request.urlopen(f'http://{ORIGIN_SERVER}:{ORIGIN_SERVER_PORT}{self.path}') as response:
                    content = response.read()
                    # default to text/html if type not found
                    content_type = response.info().get('Content-type', 'text/html')
                    self.cache_content(self.path, content, content_type)
                    self.send_content(content, content_type)

            except urllib.error.HTTPError as e:
                # cache 404 status code, & send status to client
                if e.code == 404:
                    self.cache_content(self.path, b'', 'text/html', status_code=404)
                self.send_error(e.code, e.reason)
            except urllib.error.URLError as e:
                self.send_error(502, '** Failed to fetch data from origin server **')
            except Exception as e:
                self.send_error(500, 'Internal server error')
                print(f' ** ERROR: {e} ** ')
            return
        
        # [old code for potential dns & http communication] 
        # for path `/get_server_info` return server metrics
        # elif self.path == '/get_server_info':
        #     cpu_percent = psutil.cpu_percent()
        #     memory_info = psutil.virtual_memory()
        #     load_avg = os.getloadavg()

        #     server_info = {
        #         'cpu_percent': cpu_percent,
        #         'memory_used_percent': memory_info.percent,
        #         'memory_total': memory_info.total,
        #         'load_average': load_avg,
        #     }
        #     self.send_response(200)
        #     self.send_header('Content-type', 'application/json')
        #     self.end_headers()
        #     # send server metrics to client in JSON format
        #     self.wfile.write(json.dumps(server_info).encode())
        #     return


    def send_content(self, content, content_type, from_cache=False, status_code=200):
        '''
        Sends content to client with appropriate headers and status code.
        '''
        # check if client accepts gzip encoding
        accept_encoding = self.headers.get('Accept-encoding', '')
        if 'gzip' in accept_encoding:
            # compress content & set content-encoding header
            content = zlib.compress(content)
            self.send_header('Content-encoding', 'gzip')

        # send status code & content type headers
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        
        # send cache status header
        if from_cache:
            self.send_header('X-Cache', 'HIT')
            print(f' ** Cache HIT: {self.path} ** ')
        else:
            self.send_header('X-Cache', 'MISS')
            print(f' ** Cache MISS: {self.path} ** ')
        
        self.end_headers()
        
        # send content to client, if not 404 (no content to send)
        if status_code != 404:
            self.wfile.write(content)


    def cache_content(self, path, content, content_type, status_code=200):
        '''
        Caches content and status codes in server cache. Removes least recently
        accessed content if cache is full, and refreshes cache if content is
        already present.
        '''
        if path in self.cache:
            # refresh cache by moving most recently accessed content to end
            self.cache.move_to_end(path)
        else:
            if len(self.cache) >= self.cache_size:
                # remove least recently accessed content from cache
                self.cache.popitem(last=False)
        self.cache[path] = (content, content_type, status_code)


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

    try: # run server until exception
        http_server.serve_forever()
    except:
        http_server.server_close()
        print(' ** http server stopped ** ')


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