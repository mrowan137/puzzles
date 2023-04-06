"""
Q: The cube, 41063625 (3453), can be permuted to produce two other cubes:
56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.

A: 127035954683
"""

from collections import Counter, defaultdict


def cubic_permutations(m):
    n = 1
    perm_to_cbrt = defaultdict(list)
    while True:
        print(n)
        cnt = Counter(str(n ** 3))
        k = "".join(
            [str(cnt[str(i)]) if str(i) in cnt else "0" for i in range(10)]
        )
        perm_to_cbrt[k].append(n)

        # exit condition
        if len(perm_to_cbrt[k]) == m:
            print(
                "cube roots with same permuted digits when cubed: {}".format(
                    perm_to_cbrt[k]
                )
            )
            return min(perm_to_cbrt[k]) ** 3

        n += 1


if __name__ == "__main__":
    M = 5
    print(
        "Smallest cube with exactly {} permutations that are cube: {}".format(
            M, cubic_permutations(M)
        )
    )
