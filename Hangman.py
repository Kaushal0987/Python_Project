import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)  # random word from the list words
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # set of the letters in the words
    alphabet = set(string.ascii_uppercase)  # set of all the alphabets in english language
    used_letter = set()  # set of already used letters by the user

    live = 8
    while len(word_letters) > 0 and live > 0:

        # showing the already guessed letters
        print(f"you have {live} left\n and you have already guessed these letters: ", " ".join(used_letter))

        # showing the guessed letters of the word
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("current word: ", " ".join(word_list))

        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # removing the already guessed letter from the word_letters

            else:
                live = live-1  # removing a live if the guessed letter is not in the word
                print(f"The letter '{user_letter}' is not in the word, try again")

        elif user_letter in used_letter:
            print("You have already guessed the letter, try again")

        else:
            print("Invalid character, try again")

    if live == 0:
        print(f"YOU DIED, the word was {word}")
    else:
        print(f"YAY, you have guessed the letter, {word}")


hangman()
