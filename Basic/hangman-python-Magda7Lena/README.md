# Hangman

## Story

Let's hang somebody! Implement the popular [Hangman](<https://en.wikipedia.org/wiki/Hangman_(game)>)
game. Add a full fledged game flow with a main menu and optionally some cool graphics
in the console! Some online examples:

- https://www.gamestolearnenglish.com/hangman/
- https://www.coolmathgames.com/0-hangman

## What are you going to learn?

- use lists and strings
- handle files
- use and validate user input
- handle normal and edge cases
- ASCII art

## Tasks

1. Implement the `play(word, lives)` function as a basic hangman game.
    - The function uses its parameter `word` as the word to guess and `lives` to as the number of available mistakes
    - The initial game state is displayed as `_ _ _ _ _ _ _ _` (one underscore for each letter in `word`)
    - The game state is displayed as `_ o d _ _ o o _` if letters 'd' and 'o' have been revealed
    - It is possible to make guesses, and letters that occur in the word are revealed
    - When a guessed letter does not occur in `word`, the player loses one life
    - When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens
    - When a guess is wrong (either a new or a repeated letter), the already tried missing letters are shown to the user
    - The player wins when all the letters in `word` have been revealed
    - The player loses when misses a letter for the `lives`th time (not counting repeated guesses)
    - When the player types `'quit'` as input, the program says good-bye and terminates

2. The game play is case insensitive while the word display is case sensitive
    - Both uppercase and lowercase letters are considered as valid input
    - Uppercase and lowercase letters guesses reveal the same letters (e.g. both `c` and `C` guesses reveal all the `c`s in the word, regardless of their case)
    - Letters of different cases behave as if they were the same when checking repetitions (e.g. entering `c` after a `C` would count as a repetition)
    - On the displaying side, however, letters are revealed as they originally appear in `word` (e.g. successfully guessing `c` shows `C _ _ _ c _ _ _` for `Codecool`)

3. Add ASCII art to visualize lives left.
    - The game state display is accompanied by an ASCII art depending on the lives left
    - The art sequence is adapted to the starting value of the `lives` parameter (at least between 3 and 7) - this means that the loosing picture is always the same

4. The game uses a random word from a pre-defined word collection.
    - The game randomly picks a word at each run
    - The game randomly picks a country from `countries-and-capitals.txt`

5. The program allows to play the game on different levels.
    - The game starts with a menu for picking a difficulty level. You should not change the `play()` function, though!
    - The word-pool and the number of lives depend on the chosen level

## General requirements

None

## Hints

- As strings are immutable (i.e. you cannot change its letters) it is a better idea
  to store the state of the game (like the revealed and missed letters) with the help
  of mutable structures (like lists or sets)
- You are advised to use a `set` data structure when you have a collection which cannot have duplicated elements
- Try to create a few (3-6) functions for features that are somewhat separated from the
  main process (e.g. dealing with the inputs, parts of the display, or the menu).
  Think of the input requirements and the results of these units! Add the necessary
  inputs as parameters, and return the results that is needed by the caller side!

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/team/blueprint/hangman/python), and make sure to **select or create your team**.

## Background materials

- <i class="far fa-exclamation"></i> [Strings](https://learn.code.cool/full-stack/#/../pages/python/strings)
- <i class="far fa-exclamation"></i> [User input](https://learn.code.cool/full-stack/#/../pages/python/user-input)
- <i class="far fa-exclamation"></i> [File handling](https://learn.code.cool/full-stack/#/../pages/python/file-handling)
- <i class="far fa-open_book"></i> [Sets](https://learn.code.cool/full-stack/#/../pages/python/sets)
