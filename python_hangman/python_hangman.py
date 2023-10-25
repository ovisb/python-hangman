"""Hangman module"""
import random


def get_input(message: str) -> str:
    """
    @param message: text message
    @return: word
    """
    return input(message)


def check_winner(user_word: str, winner: str) -> bool:
    """
    @param user_word: Input word from the user
    @return: check if user word is a winner
    """
    return user_word == winner


def get_random_winner() -> str:
    possible_winners = ["python", "java", "swift", "javascript"]
    return random.choice(possible_winners)
