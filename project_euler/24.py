"""
Q: A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

  012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
  0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

A: 2783915460
"""


def permutations(nums):
    # expects the passed nums is in sorted order
    if len(nums) == 1:
        return [nums]

    # build out permutations recursively
    res = []
    for i in range(len(nums)):
        res += [[nums[i]] + r for r in permutations(nums[:i] + nums[i + 1 :])]

    return res


if __name__ == "__main__":
    permutations_of_0_to_9 = permutations([i for i in range(10)])
    print(
        "Millionth lexicographic permutation of digits 0 -- 9: {}".format(
            "".join(str(d) for d in permutations_of_0_to_9[1000000 - 1])
        )
    )
