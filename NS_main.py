#!/usr/bin/env python
import re

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst= ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list  = scapy.srp(arp_request_broadcast , timeout=1 , verbose=False)[0]
    print("ip" + "                                       " + "mac adress")
    print("--------------------------------------------------------------")
    list = []
    for i in answered_list:

        print(i[1].psrc +"                               " + i[1].hwdst)
        list.append({"ip" : i[1].psrc  , "mac_address": i[1].hwdst})


    print("--------------------------------------------------------------")
    return list



print(scan("192.168.1.1/24"))