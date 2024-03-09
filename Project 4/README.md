# Project 4: Reliable Transport Protocol

## Authors:
- [Aliya Jordan](https://github.com/aliyajo)

- Starter code provided by Professor Christo Wilson at Northeastern University

## Description:
This program is to build off a UDP baseline implementation, and build it to match the reliable TCP protocol. In being reliable, this means that is is able to be responsible for ensuring data is delivered in order, no duplicates are being interchange, there is no missing data, and no errors occur. This interchange happens between two nodes: a sender and a receiver. 

## How to run:
- This program can be ran through the command line input:
    > Command Line Syntax for sending program:
        ./3700send <recv_host> <recv_port>
    
    recv_host: The domain name, or IP address of the remote host -- Required --
    recv_port: The UDP port of the remote host -- Required --

    The data from the sender is sent to the receiver using the STDIN. Transmit this data via the UDP socket. 

    > Command line syntax for receiving program:
        ./3700recv

    The reciever program prints out the data using the STDOUT. The data that it prints is identical to the data that is supplied from the sender via STDIN. 

## Design and Implementation:
- This program was implemented following the implementation strategy of building the code with each level. It was coded to pass a level (there was 8)
that each had their own characteristics it was testing of the program.

- The functions were implemented in a way that isolates the functions/characteristics that need to be implemented by the program. 
    For instance, ensuring delivery is in order, congestion control, etc are isolated in functions. 

- Throughout these levels, they were broken down on paper on what part of the TCP protocol is being asked. This was looked more into using the lecture slides which provided equations and pseudocode to help build off of these levels. 

## Functions:
-- In 3700send file -- 
-  'Sender' Class: 
    > Contructor
        Creates a sender object
    > log(message)
        This function logs a message using stderr.
    > send(message)
        This function sends a message to the remote host.
    > extract_sequence_number(data)
        This function is used to extract the sequence number from the data
    > retransmission_control(sequence):
        This function deals with the retransmission timeout control aspect of the sender. 
    > congestion_control(timeout=false)
        This function is used ti implement the congestion control algorithm. 
        Deals with multiple aspects of the congestion control
            - Timeout
            - Slow Start
            - Congestion Avoidance
    > run()
        This function runs the sender

-- In 3700recv file --
- 'Receiver' Class:
    > Constructor
        Creates a reciever object.
    > send(message)
        This function sends a message.
    > log(message)
        This function logs a message using stderr.
    > deliver_in_order()
        This function ensures that the program delivers packets in-order.
    > run()
        This functions runs the reciever.

## Challenges: 
There were many challenges since implenting TCP logic involved multiple avenues that are addressed to paint the entire picture of having this reliable protocol. 

- Some of the challenges included, but not limited to:
    > Making sure the packages are delivered in order. This involved providing two levels of security when it comes to ensuring that the packets are going to be delivered in order. 
        1. Sorting the cache being built throughout the code
        2. Making sure the deliverance of these packages are coinciding with a variable that ensures it is sequential. 

    This was a challenge since at first there was only one layer of security that I had, bulletin 1, that was being implemented. It wasn't after reading more about TCP implementation, and realizing the assumption made by just sorting the cache is that the cache is fully in sequential order. 

    For instance, the cache could have [0, 1, 4 , 3] , we then sort which creates it to be [0, 1, 3, 4]. This however is not in the sequential order. Hence why the bulletin 2 needs to be implemented. 

    > Implementing congestion control. This was resolved by following lecture slides that provided equations on how to compute. This computation involved how to determine how to implement slow start phase, and congestion avoidance. 

    In this congestion control, timeout is also implemented in this function which equation was also found on the lecture slides. 

    Where to implement timeout in an efficient way was another challenge. 

## Testing:
- Was able to test with the given configuration files that allow us to test our sender and reciever in different scenarios. Each level addressed different issues that we need to make sure both of our programs can implement the correct characteristics.

- Was able to test with our own testing file where we tested minor functions that needed to be ensure worked before inputting into the main program. This included, but not limited to testing: 
    > Extracting the sequence number from data
    > Being able to add + 1 to this sequence number
    > Sorting dictionary keys correctly
    .. etc 

## Resources:
> https://www.geeksforgeeks.org/tcp-congestion-control/

> https://educatedguesswork.org/posts/transport-protocols-intro/ 

> https://book.systemsapproach.org/congestion/tcpcc.html 

> https://web.mit.edu/6.033/2018/wwwdocs/assignments/rtp_guide.pdf 

> Lecture Slides: Transport & Congestion Control