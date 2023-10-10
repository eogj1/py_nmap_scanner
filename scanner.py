#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is an nmap automation tool")
print("<----------------------------------------->")

ip_address = input("Please enter the IP address you want to scan")
print("IP address entered was :", ip_address)
type(ip_address)

