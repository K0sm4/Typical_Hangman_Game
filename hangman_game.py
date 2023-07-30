import random
import words_list
import draw_hangman_list as draw_hangman


def choose_word():
    words = words_list.get_word_list()
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def hangman_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0
    max_attempts = len(draw_hangman(0)) - 1

    print("Witaj w grze 'Wisielec'!")
    print("Odgadnij słowo, zgadując po jednej literze na raz.")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Podaj literę: ").lower()

        if guess in guessed_letters:
            print("Już zgadłeś tę literę.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(draw_hangman(attempts))
            print(f"Nie ma litery '{guess}' w tym słowie.")

        displayed_word = display_word(word_to_guess, guessed_letters)
        print(displayed_word)

        if displayed_word == word_to_guess:
            print("Gratulacje! Odgadłeś słowo.")
            break

        if attempts == max_attempts:
            print("Przegrałeś. Wisielec powieszony!")
            print(f"Szukane słowo to: {word_to_guess}")
            break


if __name__ == "__main__":
    hangman_game()
