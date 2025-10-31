def show_intro():
    print("Welcome to Hangman!\nI have been here the whole time\n")
    

def choose_category(categories):
    print("Categories:", ", ".join(categories))
    cat = input("Choose category: ").strip().capitalize()
    return cat if cat in categories else "All"

def show_summary(result, stats, rate):
    print("Result:", result["result"], "| Points:", result["points"],
          "| Total:", stats["score"], "| Win rate:", f"{rate:.2f}%")

def play_again():
    return input("Play again? (y/n): ").lower() == "y"

def change_category():
    return input("Change category? (y/n): ").lower() == "y"
