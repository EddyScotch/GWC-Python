import random

hi = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
q = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
exit = ['Go away', 'exit', 'leave', 'bye']
y = ['yes','yeah','yea', 'sure', 'Sure', 'ok', 'Ok', 'okay', 'Okay']
n = ['No', 'no', 'Nah', 'nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]
art = [" >^..^< ", ' =^..^= < you are amazing!', ' （＾ω＾） < you are awesome!', '`·.¸¸.·´¯`·.¸><(((º>']
def Intro ():
	print ("Hello!")

Intro ()
while True:
	userInput = input(">>> Me: ")
	if userInput in hi:
		random_hi = random.choice(hi)
		print (random_hi)
		print ("What is your name?")
		userName = input(">>> Me: ")
		print ("Hi,", userName + "!")
		print ("Let's talk!")
		feeling = input ("How are you today?")
		print ("I'm feeling", feeling, "too.")
		joke = input ("Do you want to hear a joke?")
		if joke in y:
			who = input ("Knock Knock?")
			if "Who's there?" in who:
				punch = input ("Atch")
				if "atch who" in punch or "Atch who" in punch:
					print ("Bless you.")
					break
				else:
					print ("What? Nevermind.")
			else:
				print ("What? Nevermind.")
				break
	elif userInput in exit:
		print ("Ok, bye")
		break
	elif userInput in q:
		random_response = random.choice(responses)
		print (random_response)
	else:
		print ("I did not understand what you said")
		print ("Do you want to see something cool?")
		userInput2 = input(">>> Me: ")
		if userInput2 in y:
			random_art = random.choice(art)
			print (random_art)
		else:
			print ("Ok, bye")
			break
