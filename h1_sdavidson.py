import random
import string
import time


t = "to be or not to be"
testWord = ''.join(random.choice(string.ascii_lowercase + string.digits + ' ., !?;:')for i in range(len(t)))
nextWord = ''
iterations = 0
done = False

while done == False:
	print("interation: ", iterations)
	print(" ")
	print("- - - - - - - - - - - - -")
	print(" ")
	print(testWord)

	nextWord = ''
	done = True
	time.sleep(0.2)

	for i in range(len(t)):
		if testWord[i] != t[i]:
			done = False
			nextWord += random.choice(string.ascii_lowercase + string.digits + ' ., !?;:')
		else:
			nextWord += t[i]

	iterations += 1
	testWord = nextWord

print("Target matched after: ", str(iterations), " interations")
