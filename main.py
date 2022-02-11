"""
Author: @Newtoniano20
Guess the word game
"""


import random
from colorama import Fore, Style


def user_input():
    return str(input("Input your guess: "))


def check_letter(letter: str, word: str):
    in_word = False
    index_list = []
    word_list = list(word)
    for index in range(len(word_list)):
        if letter == word_list[index]:
            in_word = True
            index_list.append(index)
    if in_word:
        return True, index_list
    else:
        return False, None


def check_win(word: str, guessed: list):
    word_list = list(word)
    if guessed == word_list:
        return True
    else:
        return False


def generate_blank_guessed(word: str):
    guessed = list(word)
    for index in range(len(guessed)):
        guessed[index] = "_"
    return guessed


def main():
    ATTEMPTS = 12
    GUESSED = False
    FAILED = False
    Failed_words = []
    Failed_attempts = 0
    with open('words.txt') as f:
        words = f.readlines()
        choice = random.choice(words)[:-1]
    guessed = generate_blank_guessed(choice)
    while not GUESSED:
        print(guessed)
        word_input = user_input()
        if word_input == choice:
            break
        character_result, character_index = check_letter(letter=word_input, word=choice)
        if character_result:
            for index in character_index:
                guessed[index] = word_input
            print(f"{Fore.YELLOW} Correct!{Style.RESET_ALL}")
        else:
            Failed_words.append(word_input)
            Failed_attempts += 1
            print(f"{Fore.RED}letter: {word_input} not in word\n {Fore.CYAN}Failed Attempts: {Failed_attempts}/{ATTEMPTS} \nAttempts not in word: {Failed_words}{Style.RESET_ALL}")

        if check_win(choice, guessed):
            GUESSED = True
        if Failed_attempts >= ATTEMPTS:
            GUESSED = True
            FAILED = True
    if not FAILED:
        print(f"You won! It was: {choice}")
    else:
        print(f"You lost :( It was: {choice}")


if __name__ == '__main__':
    main()
