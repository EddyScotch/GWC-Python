import games
game_names = ["Even or odd", "Rock Paper Scissors", "Hangman", "Madlib"]

def display_games ():
    for g in game_names:
        print (g)

def evaluate_choice ():
    ask = input ("Which game do you want to play?")
    if ask == "Even or odd" or ask == "even or odd":
        games.evenorodd ()
    if ask == "Rock Paper Scissors" or ask == "rock paper scissors":
        games.rockpaperscissors()
    if ask == "Hangman" or ask == "hangman":
        games.hangman ()
    if ask == "Madlib" or ask == "madlib":
        
def main ():
    repeat = True
    while repeat:
        display_games ()
        evaluate_choice ()
        play_again = input ("Do you wish to play again (Y/N)?")
        player = True
        while player:
            if play_again == "Y" or play_again == "y":
                print ("Got it.")
                repeat = True
                player = False

            elif play_again == "N" or play_again == "n":
                print ("Ok.")
                repeat = False
                player = False

            else:
                print ("I don't understand, can you repeat your choice?")
                player = True

if __name__ == "__main__":
    main ()
