"""
Q: By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair
and specify further that leading zeroes are not permitted, neither may a
different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, find all the square anagram
word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

A: 18769
"""

from math import log10, sqrt
from itertools import combinations
from collections import Counter, defaultdict


def num_digits(n):
    # number of digits in n
    return 1 + int(log10(n))


def is_square(n):
    return int(sqrt(n)) == sqrt(n)


def test_if_anagram_pair(pair, precomputed_squares_of_length):
    w1, w2 = pair
    squares = precomputed_squares_of_length[len(w1)]

    res, r_enc = [], []
    for sq in squares:
        trial_encoding = {c: -1 for c in list(set(w1))}
        flag = True
        for i, c in enumerate(w1):
            if trial_encoding[c] != -1 and int(str(sq)[i]) != trial_encoding[c]:
                flag = False
                break

            trial_encoding[c] = int(str(sq)[i])

        # each letter must map to a different number
        if len(trial_encoding.values()) != len(set(trial_encoding.values())):
            flag = False

        if flag:
            trial_pair = [
                "".join(str(trial_encoding[c]) for c in w1),
                "".join(str(trial_encoding[c]) for c in w2),
            ]
            if (
                all(is_square(int(n)) for n in trial_pair)
                and trial_pair[0][0] != "0"  # no leading 0
                and trial_pair[1][0] != "0"
            ):
                res += [int(n) for n in trial_pair]
                r_enc.append(trial_encoding)

    return res, r_enc


def anagramic_squares():
    # precompute dict of N:squares, which gives squares with N digits
    # manually checked 14 is longest word in the file
    squares_of_length = defaultdict(list)
    for i in range(1, int(sqrt(99999999999999))):
        squares_of_length[num_digits(i**2)].append(i**2)

    # organize words by anagram
    words = []
    with open("./words.txt") as f:
        for line in f:
            line = line.replace('"', "").lower()
            words += line.split(",")

    anagrams = defaultdict(list)
    for w in words:
        letter_count = Counter(w)
        encoding = tuple(letter_count[chr(ord("a") + c)] for c in range(26))
        anagrams[encoding].append(w)

    # for each anagram set of length N:
    res = float("-inf")
    for k in anagrams:
        maybe_anagram_pairs = list(combinations(anagrams[k], 2))
        for pair in maybe_anagram_pairs:
            auto, tenc = test_if_anagram_pair(pair, squares_of_length)
            if auto:
                res = max(res, max(auto))

    return res


if __name__ == "__main__":
    print(
        "Largest square number formed by member of anagram pair: "
        + f"{anagramic_squares()}"
    )
