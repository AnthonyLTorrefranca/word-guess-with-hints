import random

moves = {
    "Something chipmunks eat":"NUT",
    # "Holy church has this": "CROSS",
    # "Even a pirate has this": "HOOK",
    # "Best move to make by a boxer": "UPPERCUT",
}
lives = 6
pairs = list(moves.items())
pair = random.choice(pairs)
hint = pair[0]
word = pair[1]
blank = ["_"] * len(word)
clean = " ".join(blank)

# print()

# print(f"{word}")

while lives > 0 and '_' in blank:
    print(f'Current life: {lives}')
    print(f'The word consist of: {' '.join(blank)}')

    guess = input("Guess one letter in secret word: ").upper()

    if len(guess) >= 2:
        print(f'You cannot enter more than two chars\n')
    elif len(guess) == 0:
        print(f'You cannot enter blank space!\n')

    for i in range(len(word)):
        if word[i] == guess:
            blank[i] = guess
        elif word[i] != guess:
            lives -= 1

    elif guess != word[i]:
        lives -= 1