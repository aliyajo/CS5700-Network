# Project 4: Reliable Transport Protocol

## Authors:
- [Aliya Jordan](https://github.com/aliyajo)


- Starter code provided by Professor Christo Wilson at Northeastern University

## Description:
This project is to implement the HTTP protocol.This involves creating a web crawler that is able to crawl throughout the given web server give. It is able to go through the links that are embedded on the web page, parses them, and then crawls throughout them. The goal is to be able to extract the secret flag on these pages. 

## How to run:
- This program can be ran through the command line input:
    - For sending program:
      
            ./crawler <-s server> <-p port> <username> <password>
    
                -s server: Optional, server
            
                -p port: Optional, port
            
                Username: Username to login into fakebook
            
                Password: Password to login into fakebook

## Design and Implementation:
- This program was implemented with the following steps:
    - Perform Login to the HTTP server successfully
        - GET and POST request
    - Extract the link from this initial login page
    - Be in a loop that continiously extracts links and crawls throughout them
        - Determine what to do based on status code

- The design involved a recursive loop when it came to getting passed the initial login page due to the concept of a crawler being able to crawl throughout a web server.
    
## Functions:
These functions maintained the functionality of creating a web crawler.
   
- read_response(ssl_socket)
  
    Reads the response from a socket object
- send_GET_request(ssl_socket, url, secondary=False)
  
    Sends a GET request to the server. 
    Is able to function dependent on whether or not it is a 
    GET request to a=the initial login page or the subsequent
    pages. 
    The difference is whether or not to include cookies.
- send_POST_request(ssl_socket, data, url)
  
    Sends a POST request to the server.
- extract_cookies(data):
  
    Extracts the set-cookie headers from the HTML response
- extract_csrf(data):
  
    Extracts the csrfmiddlewaretoken from the given data.
- extract_links(secondary=False):
  
    Extracts the links from the HTML response.
    Also is dependent on if for the initial login page or the subsequent pages. 
- extract_status_code(data):
  
    Extracts the status code from the HTTP response.
- extract_flags(data):
  
    Extracts the secret flags from the given HTML data.
    Implements re library to help extract flags appropriately.
- crawl(ssl_socket, url):
  
    Crawls the server. It does this by performing the following:
    Sending a GET request from one of the links from the 
    set of 'frontier' links. 
    Handles the appropriate status codes.
- run()
  
    This function runs the crawler

## Challenges: 
There were many challenges involving implementing HTML. Some include:

- Ensuring that there was never ending loops, causing the program to continiously run no matter the circumstance. This was an issue if the frontier was not implemented correctly, and the history of links wasn't kept up to date. If not correct, it would revisit the links it has already been to. 

- Ensuring the correct format was used to communicate with HTML browsers. This involved making sure every detail of the POST and GET requests were accurate. If not, this would prevent access to logging into 'Fakebook'

- Extracting the correct information from the HTML browser. The secret flags is when I was running into the most trouble/bugs. My original code would erase one or two items from the end of the secret flag, presenting it to be wrong. Because of this, had to utilize the re library.

## Testing:
- Testing for this project involved appropriate printing statements throughout the code. This involved printing out the individual HTML pages, and ensuring the parsing was correct. It also involved printing out the history and frontier variable to ensure these data sets were being utilized correctly.

- The server was able to send status code to tell us on the client side whether or not what we were sending was correct implementation. 

## Resources:
> https://www.jmarshall.com/easy/http/#http1.1s4

> Lecture Slides: Web

> https://en.wikipedia.org/wiki/HTTP

> https://docs.python.org/3/library/re.html 
