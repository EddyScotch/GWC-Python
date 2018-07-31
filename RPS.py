#Rock Paper Scissors


rps = ["Rock", "rock", "Paper", "paper", "scissors", "Scissors"]
win = [ ('Rock', 'Scissors'),  # who can be defeated by ROCK
        ('Scissors', 'Paper'),  # who can be defeated by SCISSORS
        ('Paper', 'Rock')]  # who can be defeated by PAPER

keepPlaying = True
while keepPlaying == True:
    import random
    userinput = input ("Rock, Paper, or Scissors?")
    computer = random.choice (rps)
    print ("I choose ", (computer))

    if userinput in rps:
        if userinput == computer:
            print ("It's a tie!")
            good2 = True
            while good2 == True:
                understand = input ("Do you want to continue? Y/N")
                if understand == "Y" or understand == "y":
                    keepPlaying = True
                    good2 = False
                elif understand == "N" or understand == "n":
                    keepPlaying = False
                    good2 = False
                else:
                    print ("I don't understand. Can you repeat your choice?")
                    good2 = True

        elif userinput == "rock" or userinput == "Rock":
            if computer == "paper" or computer == "Paper":
                print ("You lose :( ")
                good4 = True
                while good4 == True:
                    understand = input ("Do you want to continue? Y/N")
                    if understand == "Y" or understand == "y":
                        keepPlaying = True
                        good4 = False
                    elif understand == "N" or understand == "n":
                        keepPlaying = False
                        good4 = False
                    else:
                        print ("I don't understand. Can you repeat your choice?")
                        good4 = True

            if computer == "scissors" or computer == "Scissors":
                print ("You win! :) ")
                good3 = True
                while good3 == True:
                    understand = input ("Do you want to continue? Y/N")
                    if understand == "Y" or understand == "y":
                        keepPlaying = True
                        good3 = False
                    elif understand == "N" or understand == "n":
                        keepPlaying = False
                        good3 = False
                    else:
                        print ("I don't understand. Can you repeat your choice?")
                        good3 = True

        elif userinput == "paper" or userinput == "Paper":
            if computer == "Scissors" or computer == "scissors":
                print ("You lose :( ")
                good5 = True
                while good5 == True:
                    understand = input ("Do you want to continue? Y/N")
                    if understand == "Y" or understand == "y":
                        keepPlaying = True
                        good5 = False
                    elif understand == "N" or understand == "n":
                        keepPlaying = False
                        good5 = False
                    else:
                        print ("I don't understand. Can you repeat your choice?")
                        good5 = True

            if computer == "Rock" or computer == "rock":
                print ("You win! :) ")
                good6 = True
                while good6 == True:
                    understand = input ("Do you want to continue? Y/N")
                    if understand == "Y" or understand == "y":
                        keepPlaying = True
                        good6 = False
                    elif understand == "N" or understand == "y":
                        keepPlaying = False
                        good6 = False
                    else:
                        print ("I don't understand. Can you repeat your choice?")
                        good6 = True

        elif userinput == "scissors" or userinput == "Scissors":
            if computer == "paper" or computer == "Paper":
                print ("You win! :) ")
                good7 = True
                while good7 == True:
                    understand = input ("Do you want to continue? Y/N")
                    if understand == "Y" or understand == "y":
                        keepPlaying = True
                        good7 = False
                    elif understand == "N" or understand == "n":
                        keepPlaying = False
                        good7 = False
                    else:
                        print ("I don't understand. Can you repeat your choice?")
                        good7 = True

            if computer == "Rock" or computer == "rock":
                print ("You lose :( ")
                good8 = True
                while good8 == True:
                    understand = input ("Do you want to continue? Y/N")
                    if understand == "Y" or understand == "y":
                        keepPlaying = True
                        good8 = False
                    elif understand == "N" or understand == "n":
                        keepPlaying = False
                        good8 = False
                    else:
                        print ("I don't understand. Can you repeat your choice?")
                        good8 = True

    else:
        good = True
        while good == True:
            understand = input ("I don't understand. Do you want to continue? Y/N")
            if understand == "Y":
                keepPlaying = True
                good = False
            elif understand == "N":
                keepPlaying = False
                good = False
            else:
                print ("I don't understand. Can you repeat your choice?")
                good = True
