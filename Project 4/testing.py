#!/usr/bin/env -S python3 -u

outstanding_packets = {}

def cumulative_ack(sequence_numbers):
    for i in range(len(sequence_numbers)):
        if int(sequence_numbers[i]) != i:
            return sequence_numbers[i-1]
    return sequence_numbers[-1]

def checking_acknowledgement(outstanding_packets, acknowledge_sequence):
    for i in range(int(acknowledge_sequence) + 1):
        
        if str(i) in outstanding_packets.keys():
            del outstanding_packets[str(i)]
        else:
            break
    return outstanding_packets  

def main():
    sequence_numbers = [ '0000005', '0000002', '0000005', '0000004']
    print(cumulative_ack(sequence_numbers))
    acknowledge_sequence = cumulative_ack(sequence_numbers)
    outstanding_packets = {'0000000': 
                           {
                                 'data': 'packet1', 
                                 'start': 0
                            },
                            '0000001':
                            {
                                'data': 'packet2',
                                'start': 1
                            },
                            '0000002':
                            {
                                'data': 'packet3',
                                'start': 2
                            },
                            '0000003':
                            {
                                'data': 'packet4',
                                'start': 3
                            },
                            '0000004':
                            {
                                'data': 'packet5',
                                'start': 4
                            },
                            '0000005':
                            {
                                'data': 'packet6',
                                'start': 5
                            }
    }
    print(outstanding_packets)
    outstanding_packets = checking_acknowledgement(outstanding_packets, acknowledge_sequence)
    print(outstanding_packets)


if __name__ == "__main__":
    main()