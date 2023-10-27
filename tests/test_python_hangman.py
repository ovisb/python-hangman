import io

import pytest

from python_hangman.python_hangman import (
    check_winner,
    get_input,
    get_random_winner,
    has_won,
    hint,
    update_letter_list,
)


def test_get_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("python\n"))
    assert get_input("") == "python"


def test_check_winner():
    assert check_winner("python", "python")


def test_check_not_winner():
    assert not check_winner("java", "python")


def test_random_winner():
    possible_winners = ["python", "java", "swift", "javascript"]
    assert get_random_winner() in possible_winners


@pytest.mark.parametrize(
    "winner, expected",
    [
        ("python", "pyt---"),
        ("java", "jav-"),
        ("swift", "swi--"),
        ("", ""),
        ("s", "s"),
        ("py", "py"),
        ("pyt", "pyt"),
    ],
)
def test_hint(winner, expected):
    assert hint(winner) == expected


@pytest.mark.parametrize(
    "winner, expected",
    [
        ("python", True),
        ("java", True),
        ("sw---", False),
        ("pyt---", False),
    ],
)
def test_has_won(winner, expected):
    assert has_won(list(winner)) == expected


@pytest.mark.parametrize(
    "winner_tpl, expected",
    [
        (("python", "p"), "p-----"),
        (("python", "t"), "--t---"),
        (("java", "a"), "-a-a"),
        (("java", "j"), "j---"),
    ],
)
def test_update_letter_list(winner_tpl, expected):
    winner, letter = winner_tpl
    winner_hidden = ["-"] * len(winner)
    update_letter_list(winner, letter, winner_hidden)
    assert "".join(winner_hidden) == expected
