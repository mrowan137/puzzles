"""
Q: The number 145 is well known for the property that the sum of the factorial
of its digits is equal to 145:

  1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers
that link back to 169; it turns out that there are only three such loops that
exist:

  169 → 363601 → 1454 → 169
  871 → 45361 → 871
  872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

  69 → 363600 → 1454 → 169 → 363601 (→ 1454)
  78 → 45360 → 871 → 45361 (→ 871)
  540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?

A: 402
"""

from math import factorial


def digit_factorial_sum(n):
    res = 0
    while n:
        res += factorial(n % 10)
        n //= 10

    return res


def get_factorial_chain(n):
    # get the nonrepeating terms in factorial chain
    seen = []
    while not n in seen:
        seen.append(n)
        n = digit_factorial_sum(n)

    return seen


def digit_factorial_chains(upper):
    res = 0
    for i in range(upper):
        print(i)
        res += len(get_factorial_chain(i)) == 60

    return res


if __name__ == "__main__":
    M = 1000000
    print(
        "Number of digit factorial chains with start below {} ".format(M)
        + "that have exactly 60 terms in chain: {}".format(
            digit_factorial_chains(M)
        )
    )
