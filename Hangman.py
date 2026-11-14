
import random

# List of secret words
words = ["python", "computer", "programming", "coding"]

# Testing mode: Secret word fixed to python
TEST_MODE = True

if TEST_MODE:
    secret_word = "python"
else:
    secret_word = random.choice(words)

secret_word = secret_word.lower()

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 wrong guesses.")

while wrong_guesses < max_wrong_guesses:

    progress = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("\nProgress:", progress)

    guess = input("Guess a letter: ").strip().lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter a single letter.")
        continue

    # Check repeated letters
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        print("(No attempt lost)")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print(f"{guess}: Correct")
    else:
        wrong_guesses += 1
        print(f"{guess}: Wrong ({wrong_guesses}/6)")

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nYou won! The word was", secret_word)
        break

else:
    print("\nGame Over! The word was", secret_word)

print("Wrong guesses:", wrong_guesses, "/6")






# PROJECT REPORT

# HANGMAN GAME USING PYTHON

# Submitted To:
# Rungta International Skills University
# School of Computer Science and Engineering

# Course: Bachelor of Technology (B.Tech.)
# Branch: Computer Science and Engineering
# Semester: First Semester

# Project Number: 41
# Project Title: Hangman Game

# Submitted By:
# Student Name: Rajnish kumar
# Roll Number:
# Enrollment Number:01432
# Session: 2026 to 2030

# ---

#  1.⁠ ⁠Introduction

# The Hangman Game is a word guessing game developed using Python 3. In this game, the computer selects a secret word, and the player has to guess the word by entering one letter at a time.

# The player gets a maximum of 6 wrong guesses. If the player guesses all letters correctly, the player wins. Otherwise, the game ends.

#  2.⁠ ⁠Objective of the Project

# •⁠  ⁠To develop a word guessing game using Python.
# •⁠  ⁠To understand Python strings and lists.
# •⁠  ⁠To use loops and conditional statements.
# •⁠  ⁠To understand random word selection.
# •⁠  ⁠To validate user input.
# •⁠  ⁠To improve logical thinking and programming skills.

#  3.⁠ ⁠Software Requirements

# •⁠  ⁠Programming Language: Python 3
# •⁠  ⁠Code Editor: Visual Studio Code
# •⁠  ⁠Operating System: macOS
# •⁠  ⁠Module: Random

#  4.⁠ ⁠Concepts Used

#  1.⁠ ⁠Strings
#  2.⁠ ⁠Lists
#  3.⁠ ⁠While Loop
#  4.⁠ ⁠If-Else Statements
#  5.⁠ ⁠Random Module
#  6.⁠ ⁠User Input
#  7.⁠ ⁠Conditional Logic

#  5.⁠ ⁠Working of the Project

#  1.⁠ ⁠The computer selects a secret word.
#  2.⁠ ⁠The player enters one letter.
#  3.⁠ ⁠The program checks whether the letter is correct or incorrect.
#  4.⁠ ⁠Correct letters are displayed in their positions.
#  5.⁠ ⁠Wrong guesses are counted.
#  6.⁠ ⁠The player gets 6 wrong guesses.
#  7.⁠ ⁠The game displays the winning or losing message.

#  6.⁠ ⁠Source Code

# The complete Python source code is saved in the file named "Hangman.py".

#  7.⁠ ⁠Output

# The game was successfully executed in Visual Studio Code Terminal.

# Successful Output:

# •⁠  ⁠You won! The word was python.
# •⁠  ⁠Wrong guesses: 0/6

#  8.⁠ ⁠Test Cases

# Test Case| Description| Expected Result
# Test Case 1| Correct letters| Player wins
# Test Case 2| Six wrong guesses| Game Over
# Test Case 3| Invalid input| Invalid input message
# Test Case 4| Repeated letter| Already guessed message

#  9.⁠ ⁠Result

# The Hangman Game was successfully developed and executed using Python 3. The program correctly identifies guessed letters, counts wrong guesses, validates inputs, and displays the final result.

# 10.⁠ ⁠Conclusion

# This project helped me understand the basic concepts of Python programming, including strings, lists, loops, conditional statements, and random module.

# I successfully created and executed the Hangman Game in Visual Studio Code.

# Project Status: Successfully Completed.

# ---

# Submitted By:
# Name:Rajnish kumar

# Signature: rajnish kumar