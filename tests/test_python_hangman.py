import io

from python_hangman.python_hangman import check_winner, get_input


def test_get_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("python\n"))
    assert get_input("") == "python"


def test_check_winner():
    assert check_winner("python")


def test_check_not_winner():
    assert not check_winner("java")
