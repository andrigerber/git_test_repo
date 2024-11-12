from module.hangman_FP import hangman

if __name__ == "__main__":
    word = input("Enter the secret word: ").lower()
    hangman(word)
