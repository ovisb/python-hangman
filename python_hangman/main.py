"""Main module"""
from python_hangman import hello  # type: ignore


def main() -> None:
    """Main function"""
    name = input("Enter your name: ")

    print(hello(name))


if __name__ == "__main__":
    main()
