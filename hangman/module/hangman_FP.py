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
    """Zeigt den aktuellen Spielzustand an"""
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
    print(HANGMAN_PICS[len(misses)])
    print("\nSecret Word: ", end='')
    for letter in secret_word:
        if letter in correct:
            print(f"{letter} ", end='')
        else:
            print("_ ", end='')
    print("\n\nIncorrect guesses: ", ' '.join(misses))

def get_user_guess():
    """Nimmt den Benutzerinput an und validiert ihn"""
    while True:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a single valid letter.")

def hangman(secret_word):
    """Die Hauptfunktion des Hangman-Spiels"""
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

        guess = get_user_guess()

        if guess in correct or guess in misses:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            correct.append(guess)
        else:
            misses.append(guess)
