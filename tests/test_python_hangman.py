import io

from python_hangman.python_hangman import check_winner, get_input, get_random_winner


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
