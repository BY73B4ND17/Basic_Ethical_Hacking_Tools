#!/usr/bin/env python3

import scapy.all as scapy
import time
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-r","--range",dest="ip_range",help="Enter the range of IP Addresses")
	(options,arguments) = parser.parse_args()
	if not options.ip_range:
		parser.error("[!] Enter a target range of IP Addresses!")
	return options

def scan(ip_address):
	print("[+] Broadcasting ARP Request...")
	time.sleep(2)
	arp_request = scapy.ARP(pdst=ip_address)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	
	clients_list = []
	for element in answered_list:
		client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list
	
def print_results(results_list):
	print("ARP Responses Received Successfully!")
	print("")
	print("IP Address\tMAC Address\n-----------------------------------------------")
	for client in results_list:
		print(client["ip"]+"\t"+client["mac"])

options = get_arguments()
scan_result = scan(options.ip_range)
time.sleep(2)
print_results(scan_result)
