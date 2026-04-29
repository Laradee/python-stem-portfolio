import random

highScore = 100000

def play_game(highScore):
    """Play one round of the guessing game."""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break  # Exit the loop

    if highScore > attempts:
        highScore = attempts
    choice = input("Would you like to play again: ")
    if choice == "yes":
        play_game(highScore)
    else:
        print("okay, high score: ", highScore)
        
play_game(highScore)
