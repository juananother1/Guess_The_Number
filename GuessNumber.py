import random as r

number = r.randint(1, 10)
counter = 1
looper = True

while looper == True:
    print("Guess the number: ")
    guess = (int)(input())
    counter += 1

    if guess == number:
        print("You win")
        looper = False
    
    elif guess < number:
        print("Higher")

    elif guess > number:
        print("Lower")

    elif counter > 3:
        print("You loose")
        looper = False