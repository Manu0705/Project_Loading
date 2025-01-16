import random

# Function to display the current state of the word
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

# Function to check if the word is completely guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function for the Hangman game
def hangman():
    # List of words for the game
    words = ["python", "django", "algorithm", "development", "data", "programming"]
    
    # Choose a random word
    word = random.choice(words).lower()
    
    # Set of guessed letters
    guessed_letters = set()
    
    # Number of attempts before losing
    attempts = 6
    
    # Start the game
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while attempts > 0:
        # Display the current state of the word
        print("\nCurrent word: " +display_word(word, guessed_letters))
        
        # Get the player's guess
        guess = input(f"Attempts remaining: {attempts}. Guess a letter: ").lower()
        
        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has been guessed already
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is in the word
        if guess in word:
           print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            attempts -= 3
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        # Check if the player has guessed the word
        if is_word_guessed(word, guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    
    # If the player runs out of attempts
    if attempts == 0:
        print(f"\nSorry, you've run out of attempts. The word was: {word}")

# Main program to run the Hangman game
if __name__ == "__main__":
    hangman()
    
