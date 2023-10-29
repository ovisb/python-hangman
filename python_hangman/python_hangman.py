"""Hangman module"""
import random


def validate_inp(user_input: str):
    if not user_input or len(user_input) > 1:
        raise Exception("Please, input a single letter.")

    if not user_input.islower() or user_input.isnumeric():
        raise Exception("Please, enter a lowercase letter from the English alphabet.")


def get_input(message: str) -> str:
    """
    Get input from the user
    @param message: text message
    @return: word
    """
    user_input = input(message)
    validate_inp(user_input)

    return user_input


# not used
def check_winner(user_word: str, winner: str) -> bool:
    """
    Check if user_word is winner
    @param user_word: Input word from the user
    @param winner: chosen winner word
    @return: check if user word is a winner
    """
    return user_word == winner


def get_random_winner() -> str:
    """
    Select a random winner from the possible winners list
    @return: random winner
    """
    possible_winners = ["python", "java", "swift", "javascript"]
    return random.choice(possible_winners)


# not used
def hint(winner: str) -> str:
    """
    Return hint for the user, show only the first 3 characters
    @param winner: chose winner word
    @return: winner word with hidden characters
    """
    hint_range = 3
    chars = [letter if idx < hint_range else "-" for idx, letter in enumerate(winner)]
    return "".join(chars)


def update_letter_list(winner: str, user_letter: str, winner_hidden: list[str]) -> None:
    """
    Update winning hidden list with the user letter
    @param winner: chosen winner word
    @param user_letter: input letter from the user
    @param winner_hidden: hidden list of the winning letters
    """
    start = 0
    found_letter_count = winner.count(user_letter)
    for _ in range(found_letter_count):
        idx = winner.index(user_letter, start)
        winner_hidden[idx] = user_letter
        start = idx + 1


def has_won(winner_hidden: list[str]) -> bool:
    """
    Check if there is a winner
    @param winner_hidden: hidden list of the winning letters
    @return: True if winner else False
    """
    return winner_hidden.count("-") == 0


def print_game_state(winner_hidden: list[str]) -> None:
    """
    Print stage hangman
    @param winner_hidden: hidden list of the winning letters
    """
    print("".join(winner_hidden))


def play(win_lose: dict) -> None:
    """
    Play hangman
    @param win_lose: dict containing player number of wins and loses
    """
    max_attempts = 8
    winner = get_random_winner()
    winner_set = set(winner)
    user_guesses: list[str] = []
    winner_hidden = ["-"] * len(winner)

    while max_attempts > 0:
        print_game_state(winner_hidden)

        try:
            user_letter = get_input("Input a letter: ")
        except KeyboardInterrupt:
            print("Bye")
            return
        except EOFError:
            print("Bye")
            return
        except Exception as e:
            print(e)
            continue

        if user_letter in winner_hidden or user_letter in user_guesses:
            print("You've already guessed this letter")
            continue
        elif user_letter in winner_set:
            update_letter_list(winner, user_letter, winner_hidden)

            if has_won(winner_hidden):
                print(f"You guessed the word {winner}!")
                print("You survived!")
                win_lose["win"] += 1
                return
            max_attempts += 1
        else:
            print("That letter doesn't appear in the word.")

        user_guesses.append(user_letter)
        max_attempts -= 1
        print()

    print("You lost!")
    win_lose["lose"] += 1
