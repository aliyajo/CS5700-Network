# Project 3: BGP Router

## Authors:
- [Aliya Jordan](https://github.com/aliyajo)
- [Linda Quach](https://github.com/linppa)

- Starter code provided by Professor Christo Wilson at Northeastern University.

## Description:
- The goal of this project is to implement a simple BGP router in order to
  deepen our understanding of how core internet infrastucure works by giving us
  experience building & managing forwarding tables, generating route
  announcements, and forwarding data packets from internet users. In the process
  we learn to manipulate IP addresses and understand subnet mask notation & the
  purpose of network masks. We also gain more experience with managing multiple
  sockets using the select() function and poll() function.

## How to install & run:
- The router is implemented in the file `4700router`. Ensure that this file is in
  the same directory as the `run` script, `configs` directory, and `test` suite.

  The following libraries are used in this project, all of which are a part of
  the python standard library and do not need to be installed separately.

> `argparse`, `socket`, `json`, `select`, `struct`.

- Rather than testing our on a real network, we are testing it in a simulator
  implemented in a script named `run`. The simulator comes with a suite of
  configuration files in the `configs` directory that our router is able to
  handle. To run the simulator, the following command is used:

> `$ ./run [config-file]`

- Otherwise, the router can be test with the entire test suite by running the
  following command to run the `test` file:

> `$ ./test`

## Design & Implementation:
- Before implementing the router, we first needed to understand the BGP protocol
  and how it works. We also needed to understand how to manipulate IP addresses
  & understand subnet mask notation. Along with lecture slides & materials,
  external resources that we utilized throughout the project are listed below in
  the "Resources" section.

- Utilizing the test suite, we tackled the project in a linear fashion, as
  recommended by the project description: we began with basic support for
  "update", then moved to implementing support for "dump"
  and "table" messages. At this point since we were getting more familiar with
  the expextations of the project, we were able to divide the work to implement
  "withdraw", and forwarding logic/"best route" simultaneously. Finally, we
  implemented the "peering" relationship logic, and "aggregate/disaggregate"
  functionality.

- As we progessed through the project, we extracted certain bits of code into
  helper functions in attempt to make the code more readable and easier to
  debug. We also created an additional class to handle IP address manipulation.
  
## Challenges:
- Since our team had no prior experience with larger scale projects, we decided
  to test out using GitHub in a collaborative environment. It gave us more peace
  of mind knowing that either of us would not lose or overwrite the other's
  work.
  
- Initially when we began implementing the router, we had started using a simple
  dictionary as the data structure to store the forwarding table. However, we
  had run into issues with the dictionary not being able to handle multiple keys
  when we discovered the daunting scope of the project. We decided to switch to
  using a nested dictionary, which allowed us the flexibility of storing
  multiple keys and values. This decision proved beneficial as we were able to
  add more values as we progressed through the project.

## Testing:
- We tested our BGP router by utilizing the test suite provided by the
  professor, along with doing our own testing in a separate file outside of the
  project file.

  For example, testing the logic of binary conversion or CIDR notation was done
  in a separate file to ensure that the logic was correct before implementing it
  into the larger project.

- Since the test suite was quite comprehensive, we were able to test the router
  with a variety of different configurations and scenarios. This helped us think
  about the scenarios we have to consider for further tests down the line.

- The use of printed statements we're also heavily utilized so that we could
  visually see our outputs as we ran through the test suite.


## Resources:
> Computer Networks: A systems approach. Computer Networks: A Systems Approach - Computer Networks: A Systems Approach Version 6.2-dev documentation. (n.d.). https://book.systemsapproach.org/ 

> https://stackoverflow.com/questions/1942160/python-3-create-a-list-of-possible-ip-addresses-from-a-cidr-notation

> https://www.ipconvertertools.com/convert-cidr-manually-binary#google_vignette

> https://docs.netgate.com/pfsense/en/latest/network/cidr.html#:~:text=The%20CIDR%20number%20comes%20from,11111111.00000000%20in%20binary.
