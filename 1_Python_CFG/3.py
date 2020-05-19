import time

hostsPath = r"C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

website = input("Enter the name of website to be blocked: ")

file1 = open(hostsPath, 'a')
file1.write(redirect + "\t" + website)
file1.close()