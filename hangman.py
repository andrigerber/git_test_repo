import os

# ASCII Art for the hangman progress
HANGMAN_PICS = [
    '''
     ------
     |    |
          |
          |
          |
          |
    =========''', '''
     ------
     |    |
     O    |
          |
          |
          |
    =========''', '''
     ------
     |    |
     O    |
     |    |
          |
          |
    =========''', '''
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========''', '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========''', '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========''', '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ========='''
]

def display_game_state(misses, correct, secret_word):
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
    print(HANGMAN_PICS[len(misses)])
    print("\nSecret Word: ", end='')
    for letter in secret_word:
        if letter in correct:
            print(f"{letter} ", end='')
        else:
            print("_ ", end='')
    print("\n\nIncorrect guesses: ", ' '.join(misses))

def hangman(secret_word):
    correct = []
    misses = []

    while True:
        display_game_state(misses, correct, secret_word)

        if len(misses) >= len(HANGMAN_PICS) - 1:
            print("\nYou lost! The word was:", secret_word)
            break
        elif all([letter in correct for letter in secret_word]):
            print("\nCongratulations! You guessed the word!")
            break

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in correct or guess in misses:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            correct.append(guess)
        else:
            misses.append(guess)

# Starting the game
if __name__ == "__main__":
    word = input("Enter the secret word: ").lower()
    hangman(word)
