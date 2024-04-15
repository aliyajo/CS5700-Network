# Project 6; Content  Delivery Network

## Authors:
- [Linda Quach](https://github.com/linppa)
- [Aliya Jordan](https://github.com/aliyajo)


## Description:
- This project entails creating our own basic CDN implementation. This involves creating a DNS server that is able to map the clients requesting content to what we categorize as "good" replica servers. These replica servers, which are HTTP based, are then able to retrieve the content the client is requesting. This basic implementation involves strategic planning on how the CDN is able to redirect, and utilize the HTTP server to have fast performance.



## How to install & run:
> Running
- Run the Deploy Script first, here is the syntax:

      python3 ./deployCDN -p port -o origin -n name -u username -i keyfile
  - port: port number DNS server will bind to
  - origin: name of the origin server for the CDN
  - name: CDN-specific name that dns server will redirect
  - username: account name for logging in
  - keyfile: path to the private key for logging into nodes
- Run the Run Script to then run the servers, here is the syntax:
  
      python3 ./runCDN -p port -o origin -n name -u username -i keyfile
  - port: port number DNS server will bind to
  - origin: name of the origin server for the CDN
  - name: CDN-specific name that dns server will redirect
  - username: account name for logging in
  - keyfile: path to the private key for logging into nodes

- Run the Stop Script when done with program, here is the syntax:

      python3 ./deployCDN -p port -o origin -n name -u username -i keyfile
  - port: port number DNS server will bind to
  - origin: name of the origin server for the CDN
  - name: CDN-specific name that dns server will redirect
  - username: account name for logging in
  - keyfile: path to the private key for logging into nodes

## Design & Implementation:
> First Step
- Before starting the project, we needed to review CDN's and what the goals of
  the project were. Initially we were a bit confused at what parts of the CDN
  we needed to build and which parts were already provided to us. 
  
- After figuring out how to ssh into the DNS server, we implemented a very basic
  "round-robin" DNS server that just cycles through the dictionary of
  HTTP replica/cache servers. We were able to test this by running the 'dig'
  command in the terminal to see if the DNS server was returning the correct IP
  address.

- Next, we needed to implement the HTTP cache server. we initially started by
  implementing the professor's recommendation for simply having the HTTP cache
  server act as a proxy where it would fetch content from the origin server and
  then send the content to the client. 
  
  - At this point, we had a very basic DNS & HTTP servers to continue to build upon.

> Next Step
- After implementing these foundational aspects of the servers, decided to add onto
  each.

- For the DNS server, in order to ensure it was proficient in its mapping configuration,
  decided to implement a dynamic active and passive measurement determining which
  replica server to send to.
    - For passive measurement, implemented directing based on geographical location.
      When the client si requesting content, the DNS server will determine which replica
      is closest by picking the one with the closest distance. This point of the server
      involves using <a href="https://pypi.org/project/geoip2/0.1.0/">GeoIp2</a>
      These replica servers closest to the client are then put in an ordered list.
    - For active measurement, this then looked at this ordered list, and determined if
      the first in the list--which is the closest server-- is overloaded or not.
      If it is overloaded, will move on in the list, and vice versa.
      This then returns the best server
        - Overloading was determined by sending a GET request to the replica server we are
          asking information from. On the HTTP server side, it determines its load average
          and CPU percent, and sends this back as a JSON object to the DNS server.
        - These metrics are then gauged based on the following scale:
            - Syntax for Load Average: [#, #, #]
              
                If any of these numbers are above, or equal to 2, will be determined as overloaded. This number of 2 was determined by the number of cores on the server. If the load average goes above this, then this indicates the server is experiencing high load.( <a href="https://cloudlinux.zendesk.com/hc/en-us/articles/4415075883538-Understanding-the-High-Load-Average-root-cause">Understanding High Load Average</a>)
          
            - Syntax for CPU Percent: #
          
                If this number is above a 90, will then be be determined as overloaded.
    - This DNS server also implements its own version of a cache. If the client has been
      redirected before, will redirect it to the recent server previously determined. This
      cache has a time component to maintain proficiency.

- For the HTTP server, to speed up the process of fetching content from the
  origin server, we implemented a cache for content. This cache is able to store content
  that has been requested before to send to the client, instead of having to
  fetch from the origin server again. 
    - This cache is implemented in an ordered dictionary, where the key is the
      URL and the value is the content. By using an ordered dictionary, we are
      able to maintain a Least Recently Used (LRU) cache. By having this
      ordering, the most popular content will be readily available. And this also means that if
      the cache is full, the least recently used content will be removed to make
      room for new content.
    - The reason the cache has a max size is to ensure that the cache does not
      grow too large and take up too much memory.
    - When the HTTP server sends content, it will also check if the client
      request accepts gzip encoding. If it does, the content will be compressed
      before being sent to the client to save bandwidth.
    - Another note, the HTTP server will cache URL paths that return a 404
      error. According to the professor, pages that return this error will
      always return this error, so there is no need to attempt to fetch the
      content from the origin server again.


## Challenges:
- At the start of implementing the project, we needed to review our basic understanding
  of what CDN's and the big picture. In addition, the corresponding ssh keys were needed
  to access the different servers provided for this project. After some help, we were able
  to determine how to accurately SSH into the DNS and HTTP servers to start. 

- Once we were able to SSH into these different servers, being able to actually deploy our code
  became our next issue. This was resolved with using the scp command to ensure our local
  files were copied over to these servers for deployment. In addition, to test these files,
  we were able to determine the correct syntax for the commands 'dig' and 'wget'.
  
- Implenting how we wanted to map the redirection on the DNS side was challenging strategically wise. There are ways of determining how to redirect, which was resolved through communication and viewing how real-world CDN's work. This led to using both active and passive measurement.

## Testing:
- Testing the DNS server consisted of print statements & utilizing the 'dig'
  command in the terminal to see if the DNS server was returning the correct IP
  address.

- Testing the HTTP cache server consisted of using the 'wget' command in the terminal
  to see if the cache server was able to fetch content from the origin server
  and send it to the client.

## Sources Used:
- <a href='https://humanwhocodes.com/blog/2011/11/29/how-content-delivery-networks-cdns-work/'>How Content Delivery Networks Work</a> 
- <a href='https://scoutapm.com/blog/understanding-load-averages'>Understanding Load Averages</a>
- https://pythonbasics.org/webserver/
- https://pypi.org/project/dnslib/
- https://github.com/paulc/dnslib
- <a href='https://www.geeksforgeeks.org/designing-content-delivery-network-cdn-system-design/#'>Designing CDN System Design</a>
- https://pypi.org/project/psutil/
- <a href="https://cloudlinux.zendesk.com/hc/en-us/articles/4415075883538-Understanding-the-High-Load-Average-root-cause">Understanding High Load Average</a>

