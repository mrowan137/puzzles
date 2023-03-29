"""
Q: By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

A: 121313
"""


from math import log10, sqrt
from itertools import combinations


def num_digits(n):
    return int(log10(n)) + 1


def is_prime(n, memo={}):
    if n < 2:
        return False

    if n in memo:
        return memo[n]

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def replacement_positions(n, n_wildcards):
    # hand it a number and the number of wildcards,
    # hand back a list of all the nums
    combos = combinations(list(range(num_digits(n))), n_wildcards)
    res = []
    for c in combos:
        to_add = str(n)
        for i in c:
            to_add = to_add[:i] + "*" + to_add[i + 1 :]

        res.append(to_add)

    return res


def generate_digit_replacements(p):
    # p is a specifier like 1983**19*8;
    # substitute same digit into the wildcard
    # and return all the numbers
    res = [int(p.replace("*", str(n))) for n in range(10)]

    # remove nums with 0 replacements at the lead
    for r in res:
        if r == 0 or num_digits(r) != len(p):
            res.remove(r)

    return res


def prime_digit_replacements(prime_family_size):
    # find the smallest prime which produce a family
    # of `prime_family_size` primes with digits replacement

    n_digits, n_wildcards = 2, 1
    memo = {}
    seen = set()
    while True:
        m = 10 ** (n_digits - 1)
        for n in range(m, 10 * m - 1):
            if is_prime(n, memo) and not n in seen:
                seen.add(n)
                while n_wildcards < n_digits:
                    # for each possible positions of wildcards,
                    # generate the numbers and see if it's got
                    # `prime_family_size` primes

                    for p in replacement_positions(n, n_wildcards):
                        nums = generate_digit_replacements(p)
                        num_primes = sum(is_prime(num, memo) for num in nums)
                        if num_primes == prime_family_size:
                            print("Family of primes: {}".format(nums))
                            return min(nums)

                        # we already seen these nums so
                        # don't spend more time on it
                        for num in nums:
                            seen.add(num)

                    n_wildcards += 1

            n_wildcards = 1

        # initialize for the next
        n_digits += 1


if __name__ == "__main__":
    N = 8
    print(
        "Smallest prime which with replacements "
        + "produces {}-prime value family: {}".format(
            N, prime_digit_replacements(N)
        )
    )
