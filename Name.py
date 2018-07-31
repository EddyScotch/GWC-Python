# imports the ability to get a random number (we will learn more about this later!)

from random import *

aList = ['dog', 'cat', 'rabbit', 'turtle', 'bird', 'mouse', 'hamster']

aRandomIndex = randint (0, len(aList)-1)
print (aList[aRandomIndex])
