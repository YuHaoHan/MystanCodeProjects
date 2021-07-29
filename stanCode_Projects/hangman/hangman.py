"""
File: hangman.py
Name: David
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game. At the beginning, the program will pick a random word
    as the answer. Then, players are going to guess what are the word.
    Players have N_TURNS chances to guess a wrong alphabet.
    """
    task = random_word()
    initial_state = begin(task)
    # Create the initial state (all elements are dashed words)
    answer = ""
    # Create a variable to save the correct alphabets that have been guessed.
    print("The word looks like: "+str(initial_state))
    n = N_TURNS
    while True:
        """
        Use a while true loop to continue the game until players 
        get the answer or players are completely hung.
        """
        print("You have " + str(n) + " guesses left.")
        guess = enter()
        # Use enter() function to ensure players enter an alphabet in legal form.
        if task.find(guess) != -1:
            # Players answer a correct alphabet.
            new = ""
            for i in range(len(task)):
                # Replace the dash with the correct alphabet.
                if task[i] == guess:
                    new += task[i]
                    answer += guess
                    # Save the correct alphabet.
                elif answer.find(task[i]) != -1:
                    # Replace the dash with the correct alphabets that have been guessed before this round.
                    new += task[i]
                else:
                    new += "_"
            print("You are correct!")
            print("The word looks like: "+str(new))
        else:
            # Players answer a wrong alphabet.
            n -= 1
            new = ""
            for i in range(len(task)):
                if answer.find(task[i]) != -1:
                    # Replace the dash with the correct alphabets that have been guessed before this round.
                    new += task[i]
                else:
                    new += "_"
            print("There is no "+str(guess)+"'s in the word.")
            print("The word looks like: "+str(new))
        if task == new:
            # Players get the answer.
            print("You win!")
            break
        if n == 0:
            # Players are completely hung.
            print("You are completely hung : (")
            break
    print("The word was " + str(task))


def enter():
    """
    Players enter the alphabet they want to guess.
    :return: An alphabet in legal form.
    """
    while True:
        guess = input("Your guess: ")
        if len(guess) != 1:
            # Not just one element
            print("illegal format.")
        elif not guess.isalpha():
            # Not an alphabet
            print("illegal format.")
        else:
            guess = guess.upper()
            # Case-insensitive
            return guess
        

def begin(task):
    """
    Create the initial state.
    :param task: the random word that is chosen
    :return: initial state (all elements are dash)
    """
    ans = ""
    for i in range(len(task)):
        ans += '_'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
