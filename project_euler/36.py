"""
Q: The decimal number, 585 = 1001001001_2 (binary), is palindromic in both
bases. Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)

A: 872187
"""

from math import log10


def is_base10_palindrome(n):
    n_orig = n
    r = 0
    while True:
        r += n % 10
        n //= 10

        if not n:
            break

        r *= 10

    return r == n_orig


def is_base2_palindrome(n):
    n_orig = n
    r = 0
    while n:
        r <<= 1
        r += n & 1
        n >>= 1

    return r == n_orig


def sum_double_palindromes(n):
    # sum the double palindromes less than n
    res = 0
    for i in range(1, n):
        if is_base10_palindrome(i) and is_base2_palindrome(i):
            res += i

    return res


if __name__ == "__main__":
    N = 1000000
    print(
        "Sum of double (base2, base10) palindromes less than {}: "
        "{}".format(N, sum_double_palindromes(N))
    )
