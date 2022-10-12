## As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

import random as r

def play_game():
    random_number = r.randint(1, 100)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print("You have 5 tries to guess the number")
    print("Good luck!")
    print("=====================================")

    for i in range(5):
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print("You got it! You won!")
            break
        elif guess > random_number:
            print("Too high!")
        else:
            print("Too low!")
    else:
        print("You lost! The number was " + str(random_number))

    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")
