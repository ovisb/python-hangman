"""Main module"""
from python_hangman import (  # type: ignore
    check_winner,
    get_input,
    get_random_winner,
    hint,
)


def main() -> None:
    """Main function"""
    print("H A N G M A N")

    winner = get_random_winner()

    winner_hint = hint(winner)

    user_word = get_input(f"Guess the word {winner_hint}: ")

    if check_winner(user_word, winner):
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
