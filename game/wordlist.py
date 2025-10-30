import random, os

def load_categories(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return ["All", "Animals", "Countries", "Programming", "Science"]

def load_word(words_dir, category):
    if category == "All":
        path = os.path.join(words_dir, "words.txt")
    else:
        path = os.path.join(words_dir, "categories", category.lower() + ".txt")

    with open(path, "r") as f:
        words = [w.strip().lower() for w in f if w.strip().isalpha()]
    return random.choice(words)
