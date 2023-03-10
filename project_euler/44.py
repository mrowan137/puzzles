"""
Q: Pentagonal numbers are generated by the formula, P_n=n(3n−1)/2. The first ten
pentagonal numbers are:

  1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
difference are pentagonal and D = |P_k − P_j| is minimised; what is the value of
D?

A: 5482660
"""
# consider pairs (i, j) and compute the differences |P_i - P_j|,
# and sort those that are pentagonal in increasing order. With
# enough pairs, we'll find the first one for which the sum is
# also pentagonal.


def pentagon_numbers_sums_diffs(n):
    # first n pentagon numbers
    p = lambda i: i * (3 * i - 1) // 2
    pentagon_numbers = [p(i + 1) for i in range(n)]

    # store the sums and differences for pairs i, j
    diffs, sums = {}, {}

    for j in range(len(pentagon_numbers) // 2):
        for k in range(j):
            diff = pentagon_numbers[j] - pentagon_numbers[k]
            if diff in pentagon_numbers:
                diffs[(pentagon_numbers[j], pentagon_numbers[k])] = diff
                sums[(pentagon_numbers[j], pentagon_numbers[k])] = (
                    pentagon_numbers[j] + pentagon_numbers[k]
                )

    diffs_to_pair = {v: k for k, v in diffs.items()}

    for diff, pjpk in sorted(diffs_to_pair.items()):
        if sums[pjpk] in pentagon_numbers:
            return pjpk[0], pjpk[1]

    # search range would need to be increased
    return -1, -1


if __name__ == "__main__":
    # manual tries shows n = 5000 is big enough
    pj, pk = pentagon_numbers_sums_diffs(5000)
    print(
        "Pair of pentagonal numbers for which sum and difference are pentagonal"
        + " and difference is minimized: P_j={}, P_k={}".format(pj, pk)
    )
