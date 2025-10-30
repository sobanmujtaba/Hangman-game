from pathlib import Path
from game.engine import play_game
from game.wordlist import load_word, load_categories
from ui.display import show_intro, show_summary, choose_category, play_again, change_category
import datetime, json

def main():
    base = Path(__file__).parent
    log_dir = base / "game_log"
    log_dir.mkdir(exist_ok=True)

    stats_file = log_dir / "stats.json"
    if stats_file.exists():
        stats = json.loads(stats_file.read_text())
    else:
        stats = {"games": 0, "wins": 0, "losses": 0, "score": 0}

    show_intro()
    categories = load_categories(base / "words/categories")
    category = choose_category(categories)

    while True:
        word = load_word(base / "words", category)
        result = play_game(word, category)
        if result["result"] == "Quit":
            break

        stats["games"] += 1
        if result["result"] == "Win":
            stats["wins"] += 1
        else:
            stats["losses"] += 1
        stats["score"] += result["points"]
        win_rate = (stats["wins"] / stats["games"]) * 100

        game_no = stats["games"]
        gpath = log_dir / f"game{game_no}"
        gpath.mkdir(exist_ok=True)
        log_path = gpath / "log.txt"

        with open(log_path, "w") as f:
            f.write(f"Game {game_no}\n")
            f.write(f"Category: {category}\nWord: {word}\n")
            f.write(f"Guesses: {result['guesses']}\n")
            f.write(f"Wrong: {result['wrong']} ({len(result['wrong'])})\n")
            f.write(f"Result: {result['result']}\n")
            f.write(f"Points: {result['points']}\n")
            f.write(f"Total Score: {stats['score']}\n")
            f.write(f"Win Rate: {win_rate:.2f}%\n")
            f.write(f"Time: {datetime.datetime.now()}\n")

        with open(stats_file, "w") as f:
            json.dump(stats, f, indent=2)

        show_summary(result, stats, win_rate)

        if not play_again():
            break
        if change_category():
            category = choose_category(categories)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
