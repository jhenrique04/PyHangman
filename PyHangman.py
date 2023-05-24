import random
from PyH_Art import logo
from PyH_Words import word_list

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def play_hangman():
    chosen_word = random.choice(word_list)
    guessed_letters = []
    lives = 6

    print(f"{logo}\n\n")

    display = display_word(chosen_word, guessed_letters)
    print(display)

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter {guess}.")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"Wrong! You lost 1 life. Lives remaining: {lives}")

        display = display_word(chosen_word, guessed_letters)
        print(display)

        if '_' not in display:
            print("You won!")
            break

        if lives == 0:
            print(f"You lost! The word was: {chosen_word}")
            break

        from PyH_Art import stages
        print(stages[lives])

play_hangman()