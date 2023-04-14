"""
Q: The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

A: 26033 = sum([13, 5197, 5701, 6733, 8389])
"""

from math import sqrt, log10


def is_prime(n, memo):
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


def num_digits(n):
    return int(log10(n)) + 1


def valid_addition_to_prime_pair_set(i, s, memo):
    # check if joining i to s is a valid prime pair set
    if not is_prime(i, memo):
        return False

    # by assumption s is already a prime pair set, so
    # only needs checking the 2*len(s) numbers coming
    # from concatenating i on the left and the right
    joined_on_left = [i * 10 ** num_digits(p) + p for p in s]
    for n in joined_on_left:
        if not is_prime(n, memo):
            return False

    joined_on_right = [p * 10 ** num_digits(i) + i for p in s]
    for n in joined_on_right:
        if not is_prime(n, memo):
            return False

    return True


def prime_pair_set(n):
    sets = [[3]]
    i, memo = 7, {}
    while max([len(s) for s in sets]) < n:
        if is_prime(i, memo):
            print("i = {}".format(i))
            to_add = []
            for s in sets:
                if valid_addition_to_prime_pair_set(i, s, memo):
                    to_add += [s.copy()]  # add set that skips adding i
                    s += [i]  # add set that adds i

            sets += to_add
            if i < 100:
                # ansatz: the sequence starts with a prime below 100
                # if we didn't find such a set of size N, we could
                # increase the search space
                sets += [[i]]

        i += 1

    sets_of_size_n = [s for s in sets if len(s) == n]
    min_sum_set = [
        s
        for s in sets_of_size_n
        if sum(s) == min([sum(s) for s in sets_of_size_n])
    ]
    return min_sum_set[0]


if __name__ == "__main__":
    N = 5
    S = prime_pair_set(N)
    print(
        "Minimum sum for prime pair set of size N = {}: sum({}) = {}".format(
            N, S, sum(S)
        )
    )
