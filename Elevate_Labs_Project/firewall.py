from scapy.all import *
import logging

logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def packet_filter(pkt):
    if pkt.haslayer(ICMP):
        logging.warning(f"BLOCKED ICMP from {pkt[IP].src}")
        return False
    elif pkt.haslayer(TCP) and pkt[TCP].dport == 80:
        logging.warning(f"BLOCKED HTTP to {pkt[IP].dst}")
        return False
    return True

if __name__ == "__main__":
    print("[*] Starting firewall (Ctrl+C to stop)...")
    try:
        sniff(filter="ip", prn=lambda x: x.summary(), lfilter=packet_filter)
    except KeyboardInterrupt:
        print("\n[!] Firewall stopped")
