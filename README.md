# EDU project

## Project

This is _Hangman_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.12
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

This is the classic _Hangman_ game. The game has a main menu where player can choose from:
 - play the game
 - show number of game wins and loses
 - exit

In each round one word is chosen randomly by the computer and round ends if user has used all 8 tries or has won.

Have fun!

## Changelog

25.10.2023
- Initial github repo creation + project structure

25.10.2023
- Stage 1 done

25.10.2023
- started stage 2
- added input from user and check for predefined(temporary) winner
- added stage2 unit tests

25.10.2023
- started stage 3
- now the winner gets picked up randomly via random module
- the word added by the user gets checked against the random winner
- added stage3 unit tests

25.10.2023
- started stage 4
- Added function which returns the first 3 characters from the winner word and hides the remaining ones
- This is a hint presented to the user like `Guess the word swi--:`
- added stage 4 unit tests

25.10.2023
- started stage 5
- main login was refactored, stage3 hint excluded/removed
- added main game loop
  - it provided the user with 8 tries
  - the winner word is now hidden, it contains dashes instead of letters
  - now user inputs a letter instead of a word
  - letter is checked to see if it's part of the winner word
  - if true, we update the hidden word with the correct letter

27.10.2023
- started stage 6
- Now if the user gets a letter right he gets a free try

29.10.2023
- started stage 7
- added function for validating user input.
- now users try will not count as a mistake if any of the exceptions are raised
- added stage 7 unit tests

29.10.2023
- started stage 8
- added game main menu
- 
## Project status
Completed stages 8/8

### Install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
