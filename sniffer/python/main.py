# must be run with root privileges

from multiprocessing import connection
import socket
from sqlite3 import InterfaceError
import struct
import binascii



# arg 1 packet InterfaceError
# arg 2 type of connection
# arg 3 protocol
# Ref: https://en.wikipedia.org/wiki/EtherType#Values
# IP V4 0x8000
# IP V6 0x86DD

s = socket.socket(socket.AF_INET6, socket.SOCK_RAW, socket.htons(0x86DD))

####
HOST = 'localhost'
PORT = 50007 
res = socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE)
family, socktype, proto, canonname, sockaddr = res[1]
###

while True:
  packet = s.recvfrom(2048)
  ethernet_header = packet[0][0:14]
  
  eth_header = struct.unpack("!6s6s2s", ethernet_header)
  mac_dest = binascii.hexlify(eth_header[0])
  mac_source = binascii.hexlify(eth_header[1])
  
  print("Destinaltion Mac Address: {dest_addy} ".format(dest_addy = mac_dest))
  print("Source Mac Address: {source_add}".format(source_add = mac_source))
  print("Type: " + binascii.hexlify(eth_header[2]))
  
  packed_header = packet[0][14:34]
  ip_header = struct.unpack("f!12s4s4s", packed_header)
  print("Source IP: " + socket.inet_ntoa(ip_header[1]))
  print(" Destination IP:" + socket.inet_ntoa(ip_header[2]))