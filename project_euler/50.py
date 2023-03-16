"""
Q: The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

A: 997651
"""

from collections import defaultdict


def primes_less_than(n):
    # return primes less than n
    nums = list(range(2, n))

    for i in range(len(nums)):
        if nums[i] == -1:
            continue

        j = i
        while True:
            j += nums[i]

            if j >= len(nums):
                break

            nums[j] = -1

    return [m for m in nums if m != -1]


def consecutive_prime_sum(n):
    # find the prime less than n
    # that could be written as sum of most consecutive primes
    primes = primes_less_than(n)
    is_prime = defaultdict(lambda: False)
    for p in primes:
        is_prime[p] = True

    cumulative_sum_primes = [0] + [p for p in primes]
    for i in range(1, len(cumulative_sum_primes)):
        cumulative_sum_primes[i] = cumulative_sum_primes[i - 1] + primes[i - 1]

    sum_primes_from_i_to_j = lambda i, j: (
        cumulative_sum_primes[j] - cumulative_sum_primes[i]
    )

    # search starting from longest consecutive sequence;
    # when we find the first prime this way, we are done;
    # note the max window size we need to consider comes from considering
    # the smallest j such that sum(primes[0:j+1]) >= max(primes),
    # because any other window of this size will exceed the largest prime.
    # we can find it with bisection.
    l, r = 0, len(primes)
    while l < r:
        m = (l + r + 1) // 2
        if sum_primes_from_i_to_j(0, m) > primes[-1]:
            r = m - 1
        else:
            l = m

    max_window_size = m

    for window_size in range(max_window_size, -1, -1):
        for window_start in range(len(primes) - window_size):
            # indices into the cumulative sum array
            i, j = window_start, window_start + window_size
            hope_it_is_prime = sum_primes_from_i_to_j(i, j)
            if is_prime[hope_it_is_prime]:
                return hope_it_is_prime

    return -1


if __name__ == "__main__":
    N = 1000000
    print(
        "Prime less than {} that can be written as sum".format(N)
        + " of consecutive primes: {}".format(consecutive_prime_sum(N))
    )
