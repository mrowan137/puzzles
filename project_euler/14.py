"""
Q: The following iterative sequence is defined for the set of positive integers:

  n → n/2 (n is even)
  n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

A: 837799
"""


def collatz_sequence_length(n, memo):
    # it is thought (but not proven) Collatz sequence end at 1,
    # which is really an assumption in this function
    n_orig = n
    sequence_length = 0
    while n != 1:
        if n in memo:
            sequence_length += memo[n]
            break

        n = n / 2 if n % 2 == 0 else 3 * n + 1
        sequence_length += 1

    memo[n_orig] = sequence_length

    # +1 accounts for the final number in the sequence, thought to be 1
    return sequence_length + 1


def longest_collatz_sequence_under_n(n):
    # find the longest Collatz sequence length under n
    max_sequence_length, n_start = 1, 1
    memo = {}
    for i in range(1, n):
        sequence_length = max(
            max_sequence_length, collatz_sequence_length(i, memo)
        )
        if sequence_length > max_sequence_length:
            max_sequence_length, n_start = sequence_length, i

    return max_sequence_length, n_start


if __name__ == "__main__":
    n = 1000000
    max_sequence_length, n_start = longest_collatz_sequence_under_n(n)
    print(
        "Longest Collatz sequence under n = {}: {}, from n_start = {}".format(
            n, max_sequence_length, n_start
        )
    )
