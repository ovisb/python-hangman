"""Main module"""
from python_hangman import check_winner, get_input  # type: ignore


def main() -> None:
    """Main function"""
    print("H A N G M A N")

    word = get_input("Guess the word: ")

    if check_winner(word):
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
