import random
print("Welcome to Guess The Number!")
lb = int(input("Enter the lower bound of the guessing range: "))
ub = int(input("Enter the upper bound of the guessing range: "))
score = 0
timesPlayed = 0
while(True):
    chances = 3
    print(f"\nGuess the number between {lb} - {ub} (both included).\n")
    a = "Enter your guess: "
    newNum = random.randint(lb, ub)
    f = 0
    while (chances > 0):
        n = int(input(a))
        if (n == newNum):
            print("Congrat's")
            score += 1
            f = 1
            break
        elif (n < newNum):
            print("Your guess was too small")
            a = "have one more try: "
        else :
            print("Your guess was too high")
            a = "have one more try: "
        chances -= 1
    timesPlayed += 1
    if (f == 0):
        print("The number was:", newNum, ":(")
    choice = input("Enter 'q' to quit and 'enter' to play again: ")
    if (choice == 'q'):
        break

a = "times"
if timesPlayed == 1:
    a = "time"
print("You played", timesPlayed, a,"and your score is:", score)