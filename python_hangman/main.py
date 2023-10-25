"""Main module"""
from python_hangman import (  # type: ignore
    get_input,
    get_random_winner,
    print_game_state,
    update_letter_list,
)


def main() -> None:
    """Main function"""
    max_attempts = 8
    print("H A N G M A N")
    print()

    winner = get_random_winner()
    winner_set = set(winner)

    winner_hidden = ["-"] * len(winner)

    while max_attempts > 0:
        print_game_state(winner_hidden)
        user_letter = get_input("Input a letter: ")

        if user_letter in winner_set:
            update_letter_list(winner, user_letter, winner_hidden)
        else:
            print("That letter doesn't appear in the word.")

        max_attempts -= 1
        print()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
