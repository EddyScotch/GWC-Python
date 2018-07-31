from random import randint

ts = ['Im hungry', 'Look, a deer!', 'This is code', 'Blueberries','Chocolate']
fs = ['This is a Haiku', 'I dont like poems', 'Do you like turtles?', 'Coding is awesome']
fss = ['Poem is over', 'What even is life?', 'You are very cool','Go away, the end', 'I cant count syllables']

Line1 = randint(0,len(fs)-1)
Line2 = randint(0,len(ts)-1)
Line3 = randint(0,len(fss)-1)

haiku= fs[Line1] +",\n"+ ts[Line2] +",\n"+ fss[Line3] + "."
print (haiku)
