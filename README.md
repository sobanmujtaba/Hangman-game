# Hangman Game

A modular Python implementation of the classic Hangman game.  
Built to practice **file organization, modular programming, input validation, scoring, ASCII art**, and **logging** — all running from a single entry point: `main.py`.

---

## Project Structure

```

hangman_game/
├── main.py                     # Entry point
├── words/
│   ├── words.txt               # 1000+ general words
│   └── categories/
│       ├── animals.txt
│       ├── countries.txt
│       ├── programming.txt
│       └── science.txt
├── game/
│   ├── engine.py               # Core gameplay logic
│   ├── wordlist.py             # Word loading and random selection
│   └── ascii_art.py            # Hangman drawing stages
├── ui/
│   └── display.py              # Handles display messages and prompts
├── game_log/                   # Auto-created game folders and logs
└── README.md                   # You are here

````

---

## How to Run

```bash
python3 main.py
````

> Ensure you are inside the `hangman_game` folder before running.

---

##  Features

 Word guessing by:

* Single letters (`a`, `p`)
* Multiple letters in sequence (`pl`, `ple`)
* Full word guesses (`apple`)

Categories:

* Animals
* Countries
* Programming
* Science
* (All — random from all words)

Game Rules:

* 6 wrong guesses = loss
* Case-insensitive guessing
* Repeated guesses don’t penalize
* ASCII hangman updates each wrong guess
* Win when all letters are revealed

Scoring Formula:

```
Points = (Word Length × 10) − (Wrong Guesses × 5)
```

Statistics Tracked:

* Games played
* Wins / Losses
* Total score
* Win rate (%)
* Average score per game

Persistent Logging:
Each new game creates:

```
game_log/game1/log.txt
game_log/game2/log.txt
```

with:

* Chosen category
* Word (hidden during play)
* Guesses (correct/wrong)
* Result, score, timestamp, and progress trace.

---

## Technical Notes

* Uses only Python basics: functions, loops, files, and modules (no classes).
* `pathlib` for safe file and folder handling.
* Works entirely from the terminal.

---

## Example Gameplay

```
Welcome to Hangman!
Choose a category (Animals, Countries, Programming, Science):
Programming

 +---+
 |   |
     |
     |
     |
     |
=========

Word: _ _ _ _ _ _
Enter letter(s): p
Correct! Progress: p _ _ _ _ _
Remaining attempts: 6

Enter letter(s): y
Correct! Progress: p y _ _ _ _
...

You win! Word: python
Points earned: 50
Total score: 150
```

## Author

**Soban Baig** 
(539789)
