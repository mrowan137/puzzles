# https://www.untrammeledmind.com/2017/12/counterintuitive-dice-probability-how-many-rolls-expected-to-get-a-6-given-only-even-outcomes/
# Counterintuitive!
# numerical check: expected number of rolls to get a 6
#                  given all previous rolls were even
import random as random
from collections import defaultdict


def roll(N):
    d = defaultdict(int)
    for _ in range(N):
        r = -1
        length = 0
        while r != 1 and r != 3 and r != 5:
            r = random.randint(1, 6)
            length += 1
            if r == 6:
                d[length] += 1
                break
    s = 0
    for k in d.keys():
        s += k * 1.0 * d[k]
    return s / sum(d.values())


if __name__ == "__main__":
    N = 100000
    print(
        "In {} trials, expected number of rolls to get a 6 "
        "given all previous rolls were even: {:4.3f}".format(N, roll(N))
    )
