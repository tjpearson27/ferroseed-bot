import binascii
import struct
import time
from PK8 import *
from framecalc import *
from seedgen import *

def initializeDuduClient():
	try:
		#Checks flag if it's in use
		fileIn = open("communicate.bin", "rb")
		fileIn.seek(0)
		isInUse = int(fileIn.read()[0])
		fileIn.close()
		if isInUse == 1:
			return False

		outFlag = list()
		outFlag.append(1)
		outFlag.append(0)
		outFlag.append(0)

		fileOut = open("communicate.bin", "wb")
		fileOut.write(bytes(outFlag))
		fileOut.close()

		return True
	except:
		return False

def checkTimeOut():
	try:
		fileIn = open("communicate.bin", "rb")
		fileIn.seek(2)
		isInUse = int(fileIn.read()[0])
		fileIn.close()

		if isInUse == 1:
			fileOut = open("communicate.bin", "wb")
			outData = list()
			outData.append(0)
			outData.append(0)
			outData.append(0)
			fileOut.write(bytes(outData))
			fileOut.close()
			return True
		
		return False
	except:
		return False

def checkSearchStatus():
	try:
		fileIn = open("communicate.bin", "r+b")
		fileIn.seek(1)
		isInUse = int(fileIn.read()[0])
		if isInUse == 1:
			outData = list()
			outData.append(1)
			outData.append(0)
			fileIn.seek(0)
			fileIn.write(bytes(outData))
			fileIn.close()
			return True
		
		return False
	except:
		return False

def getCodeString():
	while True:
		try:
			fileIn = open("code.txt", "r+")
			code = fileIn.readline()
			fileIn.close()
			return code	
		except:
			print("File reading error occured, trying again!")



def checkDuduStatus():
	try:
		fileIn = open("communicate.bin", "rb")
		fileIn.seek(0)
		isInUse = int(fileIn.read()[0])
		fileIn.close()

		if isInUse == 1:
			return True
		else:
			return False
	except:
		return False

def getPokeData():
	fileIn = open("out.pk8", "rb")
	pk8 = bytearray(fileIn.read())
	fileIn.close()

	data = PK8(pk8)

	ec = data.getEncryptionConstant()
	pid = data.getPID()
	IV1, IV2, IV3, IV4, IV5, IV6 = data.getIVs()

	iv = [IV1, IV2, IV3, IV5, IV6, IV4]

	gen = seedgen()
	seed, ivs = gen.search(ec, pid, iv)

	return ec, pid, seed, ivs, iv