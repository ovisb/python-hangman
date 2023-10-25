"""Hangman module"""


def get_input(message: str) -> str:
    """
    @param message: text message
    @return: word
    """
    return input(message)


def check_winner(user_word: str) -> bool:
    """
    @param user_word: Input word from the user
    @return: check if user word is a winner
    """
    winner = "python"  # temporary
    return user_word == winner
