import random

words = [
    "apple", "bride", "crate", "delta", "eagle",
    "flute", "glide", "house", "input", "jolly",
    "knife", "lemon", "magic", "night", "orbit"
]

correct_letters = set()
misplaced_letters = set()
wrong_letters = set()

GRN = "\033[92m"
YEL = "\033[93m"
GRY = "\033[90m"
RST = "\033[0m"

guesses = 0
limit = 6

def welcome():
    print("Welcome. Guess the 5-letter word.")

def pick_word(pool):
    w = [w.lower() for w in pool if len(w) == 5 and w.isalpha()]
    if not w:
        exit("No valid words available.")
    return random.choice(w)

def ask_guess():
    while True:
        g = input("Your guess: ").lower().strip()
        if len(g) != 5:
            print("5 letters only.")
        elif not g.isalpha():
            print("Letters only.")
        else:
            return g

def evaluate(g, s):
    out = [None]*5
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i in range(5):
        if g[i] == s[i]:
            out[i] = f"{GRN}{g[i]}{RST}"
            counts[g[i]] -= 1
    for i in range(5):
        if out[i]:
            continue
        if g[i] in s and counts[g[i]] > 0:
            out[i] = f"{YEL}{g[i]}{RST}"
            counts[g[i]] -= 1
        else:
            out[i] = f"{GRY}{g[i]}{RST}"
    for i in range(5):
        c = g[i]
        if out[i].startswith(GRN):
            correct_letters.add(c)
        elif out[i].startswith(YEL):
            misplaced_letters.add(c)
        else:
            wrong_letters.add(c)
    misplaced_letters.difference_update(correct_letters)
    wrong_letters.difference_update(correct_letters)
    wrong_letters.difference_update(misplaced_letters)
    print("".join(out))
    return g == s

def display_letters():
    a = "abcdefghijklmnopqrstuvwxyz"
    temp = []
    for c in a:
        if c in correct_letters:
            temp.append(f"{GRN}{c}{RST}")
        elif c in misplaced_letters:
            temp.append(f"{YEL}{c}{RST}")
        elif c in wrong_letters:
            temp.append(f"{GRY}{c}{RST}")
        else:
            temp.append(c)
    print("\nGuessed:")
    print("".join(temp))
    print("-"*15)

def game():
    global guesses
    welcome()
    ans = pick_word(words)
    while guesses < limit:
        display_letters()
        g = ask_guess()
        guesses += 1
        if evaluate(g, ans):
            print(f"You got it in {guesses} tries! Word was '{ans.upper()}'.")
            return
        print(f"{limit - guesses} left.")
    print(f"Out of tries. It was '{ans.upper()}'.")

if __name__ == '__main__':
    game()
