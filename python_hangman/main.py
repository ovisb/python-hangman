"""Main module"""
from python_hangman import (  # type: ignore
    get_input,
    get_random_winner,
    has_won,
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
                return
            max_attempts += 1
        else:
            print("That letter doesn't appear in the word.")

        user_guesses.append(user_letter)
        max_attempts -= 1
        print()

    print("You lost!")


if __name__ == "__main__":
    main()
