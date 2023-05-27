"""
Q: The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

  28 = 2^2 + 2^3 + 2^4
  33 = 3^2 + 2^3 + 2^4
  49 = 5^2 + 2^3 + 2^4
  47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?

A: 1097343
"""

from math import sqrt


def is_prime(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = False
        return False

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def primes_less_than(n, primes):
    i = 0
    while i < len(primes) and primes[i] < n:
        i += 1

    return primes[:i]


def count_prime_sums(
    n, m_low, m_high, precomputed_primes, nums, sum_so_far, seen
):
    # finds the number of prime sums S(p^b) <= N, where M_low, b <= M_high
    if m_low == m_high + 1:
        print(f"{nums[2]}^2 + {nums[1]}^3 + {nums[0]}^4 = {sum_so_far}")

        # make sure the sum was not seen previously
        res = sum_so_far not in seen
        seen.add(sum_so_far)
        return res

    # calculate up to p^M_high ~= N
    res = i = 0
    while i < len(precomputed_primes) and precomputed_primes[i] ** m_high <= n:
        nums.append(precomputed_primes[i])
        res += count_prime_sums(
            n - precomputed_primes[i] ** m_high,
            m_low,
            m_high - 1,
            precomputed_primes,
            nums,
            sum_so_far + precomputed_primes[i] ** m_high,
            seen,
        )
        nums.pop(-1)
        i += 1

    return res


def answer(n, m_low, m_high):
    memo = {}
    primes = [x for x in range(2, int(sqrt(n)) + 1) if is_prime(x, memo)]
    print(f"Done calculating primes up to {int(sqrt(n)) + 1}.")

    nums, sum_so_far, seen = [], 0, set()
    return count_prime_sums(n, m_low, m_high, primes, nums, sum_so_far, seen)


if __name__ == "__main__":
    N = 50000000
    M_LOW = 2
    M_HIGH = 4
    print(
        f"Count of numbers below {N} expressible as sum of "
        + f" primes quare, prime cube, and prime fourth power: {answer(N, M_LOW, M_HIGH)}".format()
    )
