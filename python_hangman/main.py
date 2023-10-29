"""Main module"""
from python_hangman import play  # type: ignore


def main() -> None:
    """Main function"""
    print("H A N G M A N")
    print()

    win_lose = {"win": 0, "lose": 0}

    while True:
        choice = input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '
        )
        if choice == "play":
            play(win_lose)
            print()
        if choice == "results":
            print(f"You won: {win_lose['win']} times.")
            print(f"You lost: {win_lose['lose']} times.")
            print()
        if choice == "exit":
            return


if __name__ == "__main__":
    main()
