"""
Q: The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 2^6972593−1; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.

A: 8739992577
"""


def large_non_mersenne_prime():
    # get last 10 digits of a*2^p + 1
    a = 28433
    p = 7830457

    last_ten_digits = a
    for _ in range(p):
        last_ten_digits *= 2
        last_ten_digits %= 10 ** 10

    return (last_ten_digits + 1) % 10 ** 10


if __name__ == "__main__":
    print(
        "Last 10 digits of the large non-Mersenne prime "
        + "28433×2^7830457+1: {}".format(large_non_mersenne_prime())
    )
