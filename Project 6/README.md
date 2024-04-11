## Sources ##
- https://humanwhocodes.com/blog/2011/11/29/how-content-delivery-networks-cdns-work/ 
- https://pypi.org/project/haversine/ 
- https://pub.towardsai.net/top-10-python-libraries-for-geocoding-in-2022-7202001575de 
- https://docs.python.org/3/library/http.server.html 

- https://pythonbasics.org/webserver/
- https://pypi.org/project/dnslib/
- https://github.com/paulc/dnslib
- https://www.geeksforgeeks.org/designing-content-delivery-network-cdn-system-design/#
- https://pypi.org/project/psutil/


# Project 6; Content  Delivery Network

## Authors:
- [Linda Quach](https://github.com/linppa)
- [Aliya Jordan](https://github.com/aliyajo)


## Description:
- 


## How to install & run:
- `pip install dnslib`
- `pip install psutil`
- 
- 
- 
- 

## Design & Implementation:
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
  then send the content to the client. At this point, I was troubleshooting
  using the beacon website, since I was having trouble figuring out the wget
  command and I didn't fully understand curl.


## Challenges:
- At the start of imlementing the project, we needed to review our basic
  understanding of CDN's and the big picture of what the project wanted us to
  accomplish. On top of that, we were given ssh private & public keys
  the professor provided in an email, which I had no clue what to do with them,
  initially. After some help, I was able to ssh into the DNS server to start.

- There was a lot of confusing on my part about how to deploy my code on my
  local machine to the DNS server. I was able to figure out the scp command to
  copy my files over.

-

## Testing:
- Testing the DNS server consisted of print statements & utilizing the 'dig'
  command in the terminal to see if the DNS server was returning the correct IP
  address.

- Testing the HTTP cache server consisted of using the 'wget' command in the terminal
  to see if the cache server was able to fetch content from the origin server
  and send it to the client.

-