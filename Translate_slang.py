def translate (dictionary):
    for key, value in sorted(dictionary.items()):
        userinput = input (">>Enter slang:")
        if userinput in key:
            print (value)
        elif userinput not in key:
            print ("I don't know that word, sorry :(")

slang = {
"omg" : "oh my gawd",
"l8r" : "later",
"ttyl" : "talk to you later",
"gn" : "good night",
"gg" : "good game",
"w/e" : "whatever",
"smh" : "shaking my head",
"gwcsip" : "girls who code summer immersion program",
"lol" : "laugh out loud",
"imo" : "in my opinion",
"wow" : "world of warcraft",
"gtg" : "got to go"
}

translate (slang)
