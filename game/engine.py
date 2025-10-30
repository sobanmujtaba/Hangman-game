from game.ascii_art import STAGES

def play_game(word, category):
    shown = ["_" for _ in word]
    wrong, guesses = [], []
    while True:
        print(STAGES[len(wrong)])
        print("Word:", " ".join(shown))
        print("Wrong guesses:", ", ".join(wrong) if wrong else "(none)")
        print("Attempts left:", 6 - len(wrong))
        guess = input("Enter letter(s) or word ('quit' to exit): ").strip().lower()
        if guess == "quit":
            return {"result": "Quit", "word": word, "wrong": wrong, "guesses": guesses, "points": 0}
        guess = "".join(guess.split())  # merge spaced letters

        if not guess.isalpha():
            print("Invalid input. Use only letters.")
            continue

        correct = False
        if len(guess) == len(word):  # full word
            if guess == word:
                shown = list(word)
                correct = True
            else:
                wrong.append(guess)
        elif len(guess) > 1:  # multi-letter sequence
            for ch in guess:
                if ch in word:
                    for i, c in enumerate(word):
                        if c == ch:
                            shown[i] = c
                            correct = True
                else:
                    wrong.append(ch)
            if not correct:
                wrong.append(guess)
        else:  # single letter
            if guess in guesses:
                print("Already guessed.")
                continue
            if guess in word:
                for i, c in enumerate(word):
                    if c == guess:
                        shown[i] = c
                        correct = True
            else:
                wrong.append(guess)

        guesses.append(guess)

        if "_" not in shown:
            pts = max(0, int(len(word) * 100 * (1 - 0.1 * len(set(wrong)))))
            print("You win! Word:", word, "| Points:", pts)
            return {"result": "Win", "word": word, "wrong": wrong, "guesses": guesses, "points": pts}
        if len(set(wrong)) >= 6:
            print(STAGES[6])
            print("You lose! Word was:", word)
            return {"result": "Loss", "word": word, "wrong": wrong, "guesses": guesses, "points": 0}
