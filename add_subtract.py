#!/bin/py
# Python 3.4.3 

print(""" 
	Text-based program for practicing addition and subtraction problems under timed conditions and for a score. 
    	There's some overlap with multiplication_practice.py in another repo, so I'll be recycling some of the code 
	from there for this project. In the future, it's possible that the two programs will merge. 
""")

# Immport Python libraries  
from random import randint		# for pseudo-random number generation 
from time import localtime, mktime 	# for time tracker 

# Define functions 

def random_addition():
	""" Generate random addition problem for users to solve within allocated time. 
	Correct answers are awarded a single point. 
	""" 

	# Set time limit 
	time_limit = 10 

	# Initialize problem count, current score 
	count, right = 0, 0 

	print("""
	You can answer each question by typing in your repsonse and pressing the Enter key. 
	To receive credit, you'll need to answer each question correctly within %d seconds. 
	"""  % (time_limit,))

	input("Are you ready to play? For a GOOD time press the Enter key. ") # Ask user to start program
	print()

	while True: 
		count += 1
	
	# Addition logic 
		c = randint(10,20)	# Generate a pseudo-random number between 10 and 20 
		b = randint(0,c)	# Generate a pseudo-random number between 0 and c
		a = c - b 		# Make a + b = c 

	# Addition problem 
		addition_problem = '%d + %d = ' % (a,b)
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
	# Checking that the above is working 
	print(count)
	print(addition_problem, correct_answer)	
	print(start_time, user_answer, end_time)
()


# Testing 
random_addition()
random_addition()
random_addition()
