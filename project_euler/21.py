"""
Q: Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

A: 31626
"""
from math import sqrt


divisors_of = {}


def sum_of_divisors(n):
    if n in divisors_of:
        return sum(divisors_of[n])

    divisors = [1]
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            divisors += [i, n // i]

    divisors_of[n] = divisors
    return sum(divisors)


def amicable(a, b):
    return (
        True if sum_of_divisors(a) == b and sum_of_divisors(b) == a else False
    )


def amicable_numbers_less_than(n):
    amicable_numbers = set()
    for i in range(1, n + 1):
        print(i)
        for j in range(1, i):
            if amicable(i, j):
                amicable_numbers.add(i)
                amicable_numbers.add(j)

    return [x for x in amicable_numbers]


if __name__ == "__main__":
    n = 10000
    print(
        "Sum of amicable numbers less than {}: {}".format(
            n, sum(amicable_numbers_less_than(n))
        )
    )
