#!/usr/bin/env python3

import subprocess
import optparse
import time

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC Address")
	parser.add_option("-m","--mac",dest="mac_address",help="The new MAC Address value")
	(options,arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[!] Enter an interface, check --help for the manual.")
	elif not options.mac_address:
		parser.error("[!] Enter a MAC Address, check --help for the manual.")
	return options

def change_mac(interface,mac_address):
	print(f"[+] Changing MAC Address for {interface}...")
	time.sleep(2)
	print(" ")
	print(f"Shutting down the interface...")
	subprocess.call(["ifconfig",interface,"down"])
	time.sleep(2)

	print(f"Overwriting old MAC Address with new one...")
	subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
	time.sleep(2)

	print(f"Turning the interface back on...")
	subprocess.call(["ifconfig",interface,"up"])
	time.sleep(2)
	print(" ")
	choice = input("[+] MAC Address Changed. Do you want to check? (Y/N) : ")

	if choice.lower() == "y":
		subprocess.call(f"ifconfig {interface}",shell=True)
	elif choice.lower() == "n":
		print("Exiting the tool...")
		time.sleep(2)
		print("MAC Changer terminated successfully.")
		pass
		
if __name__ == "__main__":
	options = get_arguments()
	change_mac(options.interface,options.mac_address)
	

	
