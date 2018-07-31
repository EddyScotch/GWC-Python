guessed_letters = []
good = []
bad = []
game_over = False

phrase = input("Type a phrase for someone to guess: ")
phrase = phrase.lower()

display = " "
for letter in phrase:
    if letter in good:
        display += letter
    elif letter == " ":
        display += "  "
    # The letter has not been guessed yet
    else:
        display += "_ "

# Allow user to give input to computer
tries = 7
while tries > 0:
    display = " "
    for letter in phrase:
        if letter in good:
            display += letter
        elif letter == " ":
            display += "  "
        # The letter has not been guessed yet
        else:
            display += "_ "
    if tries == 0:
        print ("You ran out of tries!")
        print ("Play again!")
        break
    elif "_" not in display:
        print ("Yay! You finished the phrase!: ")
        print (display)
        print ("Play again!")
        break
    print ("Incorrect")
    print (bad)
    print ("\n")
    print (display)
    guess = input ("Enter a letter: ")

    if guess in guessed_letters or guess in bad or guess in good:
        print ("Already guessed", guess)
        guessed_letters.append (guess)
    elif guess in phrase:
        print ("You got a letter: {}".format (guess))
        good.append (guess)
    else:
        print ("{} is not in the phrase".format (guess))
        tries = tries - 1
        bad.append (guess)

    print (tries, "chances left")
    print ("\n")


# End the game if the user gets all the right letters in the word/phrase
