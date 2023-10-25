"""Hangman module"""
import random


def get_input(message: str) -> str:
    """
    Get input from the user
    @param message: text message
    @return: word
    """
    return input(message)


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


def hint(winner: str) -> str:
    """
    Return hint for the user, show only the first 3 characters
    @param winner: chose winner word
    @return: winner word with hidden characters
    """
    hint_range = 3
    chars = [letter if idx < hint_range else "-" for idx, letter in enumerate(winner)]
    return "".join(chars)
