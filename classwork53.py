import random

hasWon = False
isFirstPersonTurn = True
while(not hasWon):
    a = "Second person's turn"
    if(isFirstPersonTurn):
        a = "First person's turn"
    print(a + ", enter to play your turn!")
    input()
    c = random.randint(1, 7)
    print(a + " got " + str(c))
    if(c == 4):
        print(a + " has won!")
        hasWon = True
    isFirstPersonTurn = not isFirstPersonTurn