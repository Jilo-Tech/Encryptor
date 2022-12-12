#!/usr/bin/env python3

### Libraries ###
import os
from cryptography.fernet import Fernet
import sys
### Main ###
files =[]
for items in os.listdir():
	if items == "Encryptor.py" or items == "thekey.key":
		continue
	if os.path.isfile(items):
		files.append(items)

key = Fernet.generate_key()

def Encryption():
	with open("thekey.key","wb") as thekey:
		thekey.write(key)

	for x in files:
		with open(x,"rb") as thefile:
			contents = thefile.read()
		contents_encrypted = Fernet(key).encrypt(contents)
		with open(x,"wb") as thefile:
			thefile.write(contents_encrypted)
	print("\n Done.")

def Decryption():
	with open("thekey.key","rb") as key:
		secretkey = key.read()

	for x in files:
		with open(x,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(x,"wb") as thefile:
			thefile.write(contents_decrypted)
	print("\n Done.")

def main():
	os.system('cls')
	print("What Can i Do For You  ==> \n\n","1.Encrpt\n","2.Decrypt\n","3.Quit\n")
	answer = input("===> ")
	if answer =='1':
		Encryption()
	elif answer =='2':
		Decryption()
	elif answer =='3':
		exit()
	else:
		print("Wrong Answer Sir, Please Try Again ...")
		os.system('cls')
		main()

if __name__ == '__main__':
	main()