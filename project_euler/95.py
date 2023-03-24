"""
Q: The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we
form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding
one million.

A: 14316
"""

from math import sqrt


def sum_of_divisors(n, divisors_of={}):
    if n in divisors_of:
        return sum(divisors_of[n])

    divisors = [1]
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            divisors += [i, n // i]

    divisors_of[n] = divisors
    return sum(divisors)


def smallest_member_of_longest_amicable_chain(m):
    seen_in_a_chain = set()
    chains = []
    divisors_of = {}
    for n in range(m):
        print(n)

        if n in seen_in_a_chain:
            continue

        chain = []
        while n < m and not n in chain:
            chain.append(n)
            n = sum_of_divisors(n, divisors_of)
            if n == chain[0]:
                chains.append(chain)
                for c in chain:
                    seen_in_a_chain.add(c)

                break

    print(chains)
    return min(max(chains, key=len))


if __name__ == "__main__":
    M = 1000000
    print(
        "Smallest member of longest amicable chain: "
        + "{}".format(smallest_member_of_longest_amicable_chain(M))
    )
