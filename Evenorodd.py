import random
def evenorodd():
    computer_value = random.randint (1,10)
    print ("{}".format(computer_value))
    userinput = input("Is this number 'even' or 'odd'?")
    if ((computer_value%2) == 0) and (userinput == "even"):
        print ("YA DID IT! YOU SO SMORT \n")
    elif ((computer_value%2) == 0) and (userinput == "odd"):
        print ("You're wrong. \n")
    elif ((computer_value%2) != 0) and (userinput == "even"):
        print ("You're wrong. \n")
    if ((computer_value%2) != 0) and (userinput == "odd"):
        print ("YA DID IT! YOU SO SMORT \n")

evenorodd()
