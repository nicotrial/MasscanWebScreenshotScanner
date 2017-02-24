import time
import os
import argparse # for args and shit
from selenium import webdriver

driver = webdriver.Firefox()

def function1(keyfile):
	print("Scanning on " + keyfile)
	os.system("masscan -p80 "+ keyfile + "> ips.txt" )
	os.system("grep -oP '(?<=on )\S*' ips.txt > ips2.txt")
	file = open("ips2.txt", "r") 
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

	parser = argparse.ArgumentParser("ssh public key scanner")
	parser.add_argument("-f", help="SSH PublicKey file")
	    	
	args = parser.parse_args()
	if args.f:
		function1(args.f)	
	
if __name__ == "__main__":
	main()
