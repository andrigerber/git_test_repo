from module.hangman_OOP import Hangman  # Importiere die Hangman-Klasse aus dem Modul hangman

if __name__ == "__main__":
    word = input("Enter the secret word: ").lower()
    game = Hangman(word)
    game.play()
