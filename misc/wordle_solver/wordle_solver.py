"""Robust calculation, but probably want to parallelize for full calculation"""
import numpy as np
import random
import time

with open("words.txt") as f:
    words = f.read()
    words = words.split("\n")
    words = [w for w in words if len(w) == 5]


def colors_and_letters(guess, answer):
    colors, letters = ["b"] * 5, ["@"] * 5
    for idx in range(5):
        if guess[idx] == answer[idx]:
            colors[idx], letters[idx] = "g", guess[idx]
        elif answer.find(guess[idx]) != -1:
            colors[idx], letters[idx] = "y", guess[idx]

    return "".join(colors), "".join(letters)


def possible(w, state, memo):
    if (w, state) in memo:
        return memo[(w, state)]
    colors, letters, guesses = state

    # must have a yellow letter but not at yellow index
    for i, c in enumerate(colors):
        # must have green letter in same position
        if c == "g" and not w[i] == letters[i]:
            memo[(w, state)] = False
            return False

        # check if yellow letter at the yellow idx
        if c == "y":
            if w[i] == letters[i]:
                memo[(w, state)] = False
                return False

            # now know yellow idx does not have the yellow letter, so check
            # if it is there
            if w.find(letters[i]) == -1:
                memo[(w, state)] = False
                return False

    # black letters are in guesses, but not a yellow letter or green letter
    black_letters = [l for l in guesses if not l in letters]

    # no blacklist letter
    for i in range(5):
        if w[i] in black_letters:
            memo[(w, state)] = False
            return False

    memo[(w, state)] = True
    return True


def solve(state, possible_words):
    colors, letters, guesses = state
    memo = {}
    # trim the possible words given the current state
    i = 0
    while i < len(possible_words):
        if not possible(possible_words[i], state, memo):
            possible_words.pop(i)
        else:
            i += 1

    # assign a score to each word based on how many it eliminates
    # the guess will be the one that eliminates the most
    # word --> avg number would be eliminated
    avg_eliminated = {}

    # for each word pair of guess and answer,
    for i, guess in enumerate(possible_words):
        start = time.time()
        eliminated = 0
        for ans in possible_words:
            # clue: 'ccccc', '@@@@@',
            # 1) compute the new clue, which along with guess create state
            wouldbe_state = colors_and_letters(guess, ans) + (
                "".join([guess, "".join([g for g in guesses])]),
            )

            eliminated += sum(
                [not possible(w, wouldbe_state, memo) for w in possible_words]
            )

        print(
            f"Completed {i}/{len(possible_words)} ({time.time() - start} sec)"
        )
        avg_eliminated[guess] = eliminated / len(possible_words)

    # now the map from guess --> number of words eliminated
    # we we'll return the one that maximize the number of eliminated words
    # find the max number of words (on avg) eliminated
    m = max(avg_eliminated.items(), key=lambda item: item[1])[1]

    # best guess is one(s) that eliminates the most
    best_guesses = [item[0] for item in avg_eliminated.items() if item[1] == m]

    return best_guesses, m


if __name__ == "__main__":
    i, j = 2293, 2593
    best_guesses, eliminated = solve(
        ("bbbbb", "@@@@@", tuple(),), words[i : j + 1]
    )
    print("Best guess(es) out of word [{}, {}]: {}".format(i, j, best_guesses))
    print("Average eliminated: {}".format(eliminated))
