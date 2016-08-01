#!/bin/py
# Python 3.4.3 

# Import Python libraries  

from random import randint		# for pseudo-random number generation 
from time import localtime, mktime 	# for time tracker 


# Define functions 

def random_addition():
	""" Generate random addition problem for users to solve within allocated time. 
	Correct answers are awarded a single point. 
	""" 	
	# Define variables 

	time_limit = 10			# Set time limit 
	count, right = 0, 0 		# Initialize problem count, current score 
	
	while True: 
		count += 1
	
	# Addition logic 
		c = randint(10,20)	# Generate a pseudo-random number between 10 and 20 
		b = randint(0,c)	# Generate a pseudo-random number between 0 and c
		a = c - b 		# Make a + b = c 

	# Addition problem 
		addition_problem = ' %d + %d = ' % (a,b)
		correct_answer = c

	# Start timer 
		start_time = mktime(localtime())

	# Accept user input 
		user_answer = input("%3d." % count + addition_problem)

	# End timer 
		end_time = mktime(localtime())

	# End loop when user wants to quit 
		if user_answer.lower() == 'q': 
			count -= 1 
			break

	# If too long, answer is marked as wrong 
		if end_time - start_time > time_limit:
			print("You took too long!")
			continue  
		try: 
			if int(user_answer) == correct_answer: 
				right +=1	
				print("Right!")
			else: 
				print("Wrong!")	
						
		except: 
			print("Badness!")

	percent = round(right/count * 100.0) if count else 0 

	print("You answered % d correct out of %d." %(right, count))
	print("That\'s %d%%." % (percent,)),

random_addition()

