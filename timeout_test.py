#!/bin/bash
import time
from threading import Thread  

answer = None 

def check():
	time.sleep(2)
	if answer != None: 
		return 
	print("Too slow!")

Thread(target = check).start()

answer = input("Type something: ")

