import random

# List of words to choose from
word_list = ["python", "hangman", "programming", "developer", "algorithm", "computer", "software", "debugging"]

# Function to select a random word
def get_random_word():
    return random.choice(word_list)

# Function to play the game
def play_hangman():
    # Set up initial variables
    word = get_random_word()  # Select a random word
    guessed_letters = []  # List to track guessed letters
    max_incorrect_guesses = 6  # Maximum number of incorrect guesses allowed
    incorrect_guesses = 0  # Track the number of incorrect guesses
    word_display = ['_'] * len(word)  # Display the word with blanks

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("You have 6 incorrect guesses allowed.")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        print("\nWord: " + ' '.join(word_display))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print("Guessed letters: " + ', '.join(guessed_letters))
        
        # Prompt for a letter guess
        guess = input("Guess a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            # Update word display with the correct letter
            for index, letter in enumerate(word):
                if letter == guess:
                    word_display[index] = guess
        else:
            incorrect_guesses += 1
            print(f"Oops! {guess} is not in the word.")
        
        # Check if the word is completely guessed
        if "_" not in word_display:
            print("\nCongratulations! You've guessed the word:", word)
            break

    # End of game message
    if incorrect_guesses == max_incorrect_guesses:
        print("\nGame over! You've run out of guesses.")
        print(f"The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
