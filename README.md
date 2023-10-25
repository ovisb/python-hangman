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

_Hangman_ is a simple Python cli game.

To add...

## Changelog

25.10.2023
- Initial github repo creation + project structure

25.10.2023
- Stage1 done

25.10.2023
- started stage2
- added input from user and check for predefined(temporary) winner
- added stage2 unit tests

25.10.2023
- started stage3
- now the winner gets picked up randomly via random module
- the word inputed by the user gets checked against the random winner
- added stage3 unit tests

25.10.2023
- started stage4
- Added function which returns the first 3 characters from the winner word and hides the remaining ones
- This is a hint presented to the user like `Guess the word swi--:`
- added stage 4 unit tests

#### Project status
Completed stages 4/5

#### Install steps

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

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
