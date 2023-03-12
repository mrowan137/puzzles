"""
Q: The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

A: 296962999629
"""

from math import sqrt


def digits_vector(n):
    # return a vector indicating digits present in n
    digits = [0] * 10
    while n:
        digits[n % 10] += 1
        n //= 10

    return digits


def is_prime(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 2:
        return False

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def prime_permutation_sequences():
    # find sequence of 3 4-digit numbers that are
    #   (i) prime
    #   (ii) permutations of each other

    # this is the range of 4 digit numbers,
    # and spacing for arithmetic sequence
    start, end, delta = 1000, 9999, 1

    res = []
    while start + 2 * delta <= end:
        print("delta = {}".format(delta))
        # from each valid starting number, get the sequence
        # and check if it's all prime, and permutations

        seen_primes = {}
        for n in range(start, end - 2 * delta + 1):
            sequence = [n, n + delta, n + 2 * delta]
            prime_sequence = [is_prime(n, seen_primes) for n in sequence]
            permutation_sequence = (
                digits_vector(sequence[0])
                == digits_vector(sequence[1])
                == digits_vector(sequence[2])
            )

            if all(prime_sequence) and permutation_sequence:
                res.append(sequence)

        delta += 1

    return res


if __name__ == "__main__":
    ans = prime_permutation_sequences()
    print("Length-3 sequences of 4-digit prime permutations:\n")
    for seq in ans:
        print("  {}".format("".join(str(n) for n in seq)))
