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
