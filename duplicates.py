
# Declare variables

mylist = [2,3,1,3,5]   # Our inputs to the program

has_duplicates = False # initialize as false (why?)


mylist.sort ()

for ml in mylist:
    print (ml)

print ()
for index in range (len (mylist) - 1): #range (4)
    print (index)
    print (mylist [index], mylist [index + 1])

    if (mylist[index]) == (mylist [index +1]):
        has_duplicates = True
        break

print(has_duplicates) # Our outputs of the program
