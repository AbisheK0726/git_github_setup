# Create a little program that ask the user for the following details:
# - name
# - height
# - favourite_color
# - secret_spirit_animal

# Then print out a message tailored to the user, excluding the secret_spirit_animal.
# print the first and last letter of the secret_spirit_animal and print the number of letters in the secret_spirit_animal.
# Allow the user to guess the secret_spirit_animal, if they guess correctly, print out a message saying they guessed correctly.

def play_game():
    name = input("What is your name? ")
    height = input("What is your height? ")
    favourite_color = input("What is your favourite color? ")
    secret_spirit_animal = input("What is your secret spirit animal? ")

    print("\n=====================================\n")
    
    print("Hello " + name + "!")
    print("Your height is " + height + "!")
    print("Your favourite color is " + favourite_color + "!")
    
    print("\n=====================================\n")

    print("The first letter of your secret spirit animal is " + secret_spirit_animal[0] )
    print("The last letter of your secret spirit animal is " + secret_spirit_animal[-1] )
    print("The number of letters in your secret spirit animal is " + str(len(secret_spirit_animal)))
    
    print("\n=====================================\n")

    guess = input("would you like to guess the secret spirit animal? (y/n): ")
    if guess == "y":
        guess = input("What is your guess? ")
        if guess == secret_spirit_animal:
            print("OMG how did you know?! :D")
        else:
            print("OMG how did you not know your own secret spirit animal ?! :(")
    else:
        print("Thanks for letting me know!")
        
def main():
    play_game()
    
if __name__ == "__main__":
    main()