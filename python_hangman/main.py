"""Main module"""
from python_hangman import check_winner, get_input, get_random_winner  # type: ignore


def main() -> None:
    """Main function"""
    print("H A N G M A N")

    user_word = get_input("Guess the word: ")

    winner = get_random_winner()

    if check_winner(user_word, winner):
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
