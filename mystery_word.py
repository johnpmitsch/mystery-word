import random
import string


def open_file(file_input):
    words = [line.strip() for line in open(file_input)]
    return words


def get_random_word():
    words = open_file('/usr/share/dict/words')
    random_word = random.choice(words)
    return random_word


def word_length(word):
    length = len(word)
    print("The computer's word is {} letters".format(length))
    return length


def valid_user_input(user_guess):
    if len(user_guess) > 1:
        return False
    elif user_guess in string.punctuation:
        return False
    else:
        return True


def guess_in_word(guess, random_word):
    lowercase_guess = guess.lower()
    for character in random_word:
        if lowercase_guess == character:
            return True
            user_guesses.extend(lowercase_guess)
            break
    return False


def hide_letters(user_guesses, random_word):
    word_display = []
    for character in random_word:
        if character in user_guesses:
            word_display.extend(character)
        else:
            word_display.extend("_")
    return word_display


def check_guesses_remaining(guesses_remaining):
    if guesses_remaining > 0:
        return True
    else:
        return False


def win_game(user_guesses, random_word):
    for character in random_word:
        if character not in user_guesses:
            return False
            break
    return True


def not_guessed_before(user_guess, user_guesses):
    if user_guess in user_guesses:
        return False
    else:
        return True


def validate_guess(user_guess, user_guesses):
    if valid_user_input(user_guess):
        if not_guessed_before(user_guess, user_guesses):
            return True
        else:
            print("You already guessed that letter!")
            return False
    else:
        print("That is not a one letter guess!")
        return False


def display_word(user_guesses, random_word):
    word_display = hide_letters(user_guesses, random_word)
    print('')
    for character in word_display:
        print(character, end=" ")
    print('')
    return word_display


def word_difficulty(user_input):
    word = get_random_word()
    if user_input.lower() == 'easy':
        while len(word) < 4 or len(word) > 6:
            word = get_random_word()
        return word
    elif user_input.lower() == 'normal':
        while len(word) < 6 or len(word) > 10:
            word = get_random_word()
        return word
    elif user_input.lower() == 'hard':
        while len(word) <= 10:
            word = get_random_word()
        return word
    else:
        user_input = input("Please type 'easy', 'normal', or 'hard': ")
        return word_difficulty(user_input)


def play_again(user_input):
    if user_input == 'y':
        initialize_game()
        return True
    elif user_input == 'n':
        return False
    else:
        return play_again(input("Play again? Y or N: ").lower())


def initialize_game():
    global guesses_remaining, user_guesses, new_game
    guesses_remaining = 8
    user_guesses = []
    new_game = True


initialize_game()

if __name__ == '__main__':

    while new_game:

        print("Welcome to Mystery Word")
        user_input = input("Would you like to play "
                           "EASY, NORMAL, or HARD mode: ")
        random_word = word_difficulty(user_input)
        word_length(random_word)

        while True:

            display_word(user_guesses, random_word)

            if check_guesses_remaining(guesses_remaining):
                print('')
                print("You have {} guesses".format(guesses_remaining))
                user_guess = input("Please guess a letter "
                                   "(enter QUIT to quit): ").lower()
                print('')

                if user_guess.lower() == 'quit':
                    new_game = False
                    break

                if validate_guess(user_guess, user_guesses):
                    user_guesses.extend(user_guess)

                    if guess_in_word(user_guess, random_word):
                        print("Guess is correct! {} is in the "
                              "computer's word".format(user_guess))
                    else:
                        print("Sorry, {} is not in the "
                              "computer's word.".format(user_guess))
                        guesses_remaining -= 1
            else:
                print("No guesses remaining, the computer wins!")
                print("The word was {}".format(random_word))
                new_game = play_again(input("Play again? Y or N: ").lower())
                break

            if win_game(user_guesses, random_word):
                print("YOU WIN!!! \n" * 10)
                print("The word was {}".format(random_word))
                new_game = play_again(input("Play again? Y or N: ").lower())
                break
