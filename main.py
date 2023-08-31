# **** Number Guessing App ****
from random import randint
from arts import logo
import os

# Global Constants
DIFFICULTY_LEVEL_TURNS = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

def is_linux():
    return os.name == "posix"

def clear():
    os.system("clear") if is_linux() else os.system("cls")

def display_welcome_message():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def check_answer(guess, answer):
    
    """Check answer against guess. Return 'False' if the guess is either too high or 
    too low. Return 'True' if the guess matches the answer."""
    
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer is {answer}.")
        return True
        
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")
    
    while not (level == "easy" or level == "medium" or level == "hard"):
        print("Please, choose a valid difficulty level.")
        level = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")

    return DIFFICULTY_LEVEL_TURNS[level]
    
def play_game():
    
    display_welcome_message()
    answer = randint(1, 100)
    turns = set_difficulty()
    is_user_wrong = True
    
    while is_user_wrong and turns > 0:
        
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if check_answer(guess, answer):
            is_user_wrong = False
        else:
            turns -= 1
            if turns == 0:
                print("You've run out of guesses, you lose.")
            else:
                print("Hold on, and guess again.")
    
    if input("Do you want to play the Number Guessing Game again? Type 'y', or 'n': ") == "y":
        clear()
        play_game()
    else:
        clear()
        print("Bye bye!")
    
play_game()

