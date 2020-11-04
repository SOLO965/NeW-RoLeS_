import os
import socket
import sys 

print("________________________________________		 	 	 ")
print("| |/ /\ \      / / \  |  _ \_   _| | | |				 ")
print("| ' /  \ \ /\ / / _ \ | |_) || | | |_| |			 	 ")
print("| . \   \ V  V / ___ \|  _ < | | |  _  |				 ")
print("|_|\_\   \_/\_/_/   \_\_| \_\|_| |_| |_|				 ")
	                                        
print("__        ___  ______      ___        ____   __ _     ")
print("\ \      / / |/ /  _ \    / \ \      / /\ \ / // \    ")
print(" \ \ /\ / /| ' /| |_) |  / _ \ \ /\ /    \ V // _ \   ")
print("  \ V  V / | . \|  _ <  / ___ \ V  V /    | |/ ___ \  ")
print("   \_/\_/  |_|\_\_| \_\/_/   \_\_/\_/     |_/_/   \_\ ")


print("========================================================")
print("========================================================")
print(" ____          ____   ___  _     ___  ") 
print("| __ ) _   _  / ___| / _ \| |   / _ \ ")
print("|  _ \| | | | \___ \| | | | |  | | | |")
print("| |_) | |_| |  ___) | |_| | |__| |_| |")
print("|____/ \__, | |____/ \___/|_____\___/ ")
print("       |___/            			     ")



print("1) Information Gathering")
print("2) Scanning")
print("3) DDos")

Choice = input("Enter Your Choice ==> ")

if Choice == "1":
	os.system('php rhawk.php')
if Choice == "2":
	print("====================================================================================")
	print("new scan -sV = scanning port Vesion")
	print("new scan -sP = Should IP Is Real Or Online")
	print("new scan -sneaky = Scanning a Big Website without Take The Alert (Take a long time) ")
	print("new scan -pS = scanning port from start to end ")
	print("new scan -oS = scanning Opreation System ")
	print("====================================================================================")
	nmap_scanning_for_ip = input("Enter Your Choice ==> ")

		#Scan Port Version
	if nmap_scanning_for_ip == "new scan -sV" or "new scan -sV ":
		nmap_scanning_for_ip_for_first_input = input("Enter Your Target IP: ")
		os.system('clear')
		os.system('nmap -sV ' + nmap_scanning_for_ip_for_first_input)

		#scan Port
	if nmap_scanning_for_ip == "new scan -sP" or "new scan -sP ":
		nmap_scanning_for_ip_for_two_input = input("Enter Your Target IP: ")

		os.system('nmap -sP '+ nmap_scanning_for_ip_for_two_input)
		#Sneaky
	if nmap_scanning_for_ip == "new scan -sneaky" or "new scan -sneaky ":
		nmap_scanning_for_ip_for_three_input = input("Enter Your Target IP: ")
		#T0
		os.system('nmap -T0 ' + nmap_scanning_for_ip_for_three_input)
	if nmap_scanning_for_ip == "new scan -pS" or "new scan -pS ":
		nmap_scanning_for_ip_for_four_input = input("Enter Your Target IP: ")
		os.system('nmap -p 20-10000 ' + nmap_scanning_for_ip_for_four_input)
		#Opreation System
	if nmap_scanning_for_ip == "new scan -O" or "new scan -O ":
		nmap_scanning_for_ip_for_five_input = input("Enter Your Target IP: ")

		os.system('nmap -O ' + nmap_scanning_for_ip_for_five_input)

if Choice == "3":
	os.system('python ddos-attack.py')