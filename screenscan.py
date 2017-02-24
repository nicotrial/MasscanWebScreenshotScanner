import time
import os
import argparse # for args and shit
from selenium import webdriver
from random import randint

color = "\033["+str(randint(90,99))+"m"
banner = u''''''+color+'''

             ░░            ░▒▒▒▒▒▒░                          ▓▓▓▓
   ░░       ░▒░            ▒▓▒▒▒▒▓▒               ▓▓▓        ▓▓▓▓
   ▒▓░      ▒▒  ░▒▒▒▒▒▒░   ▒▒    ▒▒             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   ░▓▒  ░░  ▒▓░ ░▓▓▒▒▒▒░   ▒▒ ░▒▒▒░             ▓             ▓▓▓▓▓
    ▒▒  ▓█░ ░▓▒  ▒▓▓▓▒░    ░▓████▓▒▒▒▒▒░      ▓▓▓▓ ▓  ▓▓▓▓▓▓▓     ▓▓▓▓
    ▒▒ ░██▓░ ▒▒  ▓███▒░     ▓██▓▒▒▒▒▒▒██░    ▓  ▓▓ ▓  ▓▓    ▓     ▓  ▓▓
    ▒▓▒▓▓▒▓▓░▒▒  ▓█▒░       ▒▒      ░▒██░   ▓▓  ▓▓ ▓  ▓▓▓▓▓▓▓     ▓   ▓
    ░▓▓▒░ ░▓▓█▓  ▒▒         ▒▓▒▒▒▒▒▒▓▓▒░    ▓   ▓▓ ▓              ▓   ▓
     ░░    ░▒█▓ ░▓▓▒▒▒▒▒▒░  ▒▓▒▒▒▒▒▒▒░  ▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓
             ░░ ░▒▒▒▒▒▒▒▒░  ░░
             
                                                                     
\033[0m'''

driver = 0

def function1(keyfile):
	global driver	
	print("Scanning on " + keyfile)
	os.system("masscan -p80 "+ keyfile + "> ips.txt" )
	os.system("grep -oP '(?<=on )\S*' ips.txt > ips2.txt")
	file = open("ips2.txt", "r") 
	driver = webdriver.Firefox()	
	driver.set_window_size(1024, 768) # set the window size that you need 	
	for line in file: 
		print (line) 
		#os.system("firefox " + line)
		try:		
			driver.get("http://"+line)
			driver.save_screenshot(line+'image.png')
		except:
			pass	
	file.close()
	driver.quit()

def main():

	parser = argparse.ArgumentParser("Website Scanner")
	parser.add_argument("-i", help="IP to Scan")
	    	
	args = parser.parse_args()
	if args.i:
		function1(args.i)	
	
if __name__ == "__main__":
	print(banner)
	main()
