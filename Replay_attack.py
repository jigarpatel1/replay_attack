#Script to change the packet data or information
from subprocess import check_output
import subprocess
import pcap,dpkt
from scapy.all import *
import sh
#below is to check all ips that are active in the network

ip = check_output(['hostname', '--all-ip-addresses'])
ip= ip.rsplit('.',1)[0]
strs=""
for num in range(1,40):
    ips=ip+"."+str(num)
    try:
        sh.ping(ips,"-c 1",_out="/dev/null")
        print(ips)
        strs=strs+ips
    except sh.ErrorReturnCode_1:
        pass  
print("Press ctrl+c")
a=sniff()
a.nsummary()
pc = pcap.pcap()     # construct pcap object
#Here, instead of tcp you can add any protocol.
#It will capture the packet in the network
pc.setfilter('tcp') # filter out unwanted packets
for timestamp, packet in pc:
    print (dpkt.ethernet.Ethernet(packet))
    for ptime,pdata in pc:
        ptime = int(ptime)
        p=dpkt.ethernet.Ethernet(pdata)
        print(p)
#Enter the data you need to change
        data=raw_input("Enter the Data: ")
#Instead of 127.0.0.1 you can put any ip from the ip list
        enter_ip=raw_input("Enter the destination ip whose packet information you want to change")
        a = IP(dst=enter_ip) / TCP() / Raw(load=data)
#It will send the packets again
        sendp(a)
