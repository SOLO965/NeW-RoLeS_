import socket
import os 
import sys


# Code Time For Scan

print(" ____          ____   ___  _     ___  ") 
print("| __ ) _   _  / ___| / _ \| |   / _ \ ")
print("|  _ \| | | | \___ \| | | | |  | | | |")
print("| |_) | |_| |  ___) | |_| | |__| |_| |")
print("|____/ \__, | |____/ \___/|_____\___/ ")
print("       |___/            			     ")


first_input_For_nmap = input("Enter Your Target IP : ")

print("new rules scan (ip) = Normal Scan")
print("new rules -sV (ip) = Port Scan Version")
print("new rules -sP (ip) = Should (ip) Is Real Or Online")
print("new rules from T0 or T5 = Time And Secuirty if you take T0 You Will Slow But You Will Skip The Firewill") 
print("new rules -C -F -I (ip) = Create a File 80 Line Of Information Gathering for The IP ")
print("new rules -v -A = Scan A Website So Fast But Your IP Will be In LogFile {vpn for safe} ")

#Varable's
first_input = input("new rules scan")
two_input = input("new rules -sV")
three_input = input("new rules -sP")
four_input = input("new rules T0")
five_input = input("new rules -C -F -I")
six_input = input
if first_input_For_nmap == (first_input):
	ip_for_first_input = input("Enter Your Target ip : "):
		os.system('clear')
		os.system('nmap ' ip_for_first_input)
		time.sleep(3)
		return first_input_For_nmap 

