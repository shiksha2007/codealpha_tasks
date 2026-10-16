import random

# List of 5 predefined words
words = ["python", "school", "circle", "coding", "animal"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("==============================")
print("       WELCOME TO HANGMAN")
print("==============================")
print("Guess the word one letter at a time!")
print("You have only 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Check whether the word is complete
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Take a letter from the player
    guess = input("Enter a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You have already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Display the final result
if wrong_guesses == max_wrong_guesses:
    print("\nGame over! The word was:", word)

print("\nThank you for playing Hangman!")