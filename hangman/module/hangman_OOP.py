import os

class Hangman:
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

    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.correct_guesses = []
        self.incorrect_guesses = []

    def display_game_state(self):
        os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
        print(self.HANGMAN_PICS[len(self.incorrect_guesses)])
        print("\nSecret Word: ", end='')
        for letter in self.secret_word:
            if letter in self.correct_guesses:
                print(f"{letter} ", end='')
            else:
                print("_ ", end='')
        print("\n\nIncorrect guesses: ", ' '.join(self.incorrect_guesses))

    def get_guess(self):
        while True:
            guess = input("\nGuess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
            elif guess in self.correct_guesses or guess in self.incorrect_guesses:
                print("You already guessed that letter.")
            else:
                return guess

    def play(self):
        while True:
            self.display_game_state()

            if len(self.incorrect_guesses) >= len(self.HANGMAN_PICS) - 1:
                print("\nYou lost! The word was:", self.secret_word)
                break
            elif all([letter in self.correct_guesses for letter in self.secret_word]):
                print("\nCongratulations! You guessed the word!")
                break

            guess = self.get_guess()

            if guess in self.secret_word:
                self.correct_guesses.append(guess)
            else:
                self.incorrect_guesses.append(guess)
