"""
Q: A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1
or 89.

How many starting numbers below ten million will arrive at 89?

A: 8581146
"""


def square_digit_sum(n):
    res = 0
    while n:
        res += (n % 10) ** 2
        n //= 10

    return res


def square_digit_chains(n):
    cnt = 0
    memo = {}  # allows skip to 1 or 89 if hit a seen number
    for i in range(1, n):
        print(i)

        m, chain = i, [i]
        while True:
            if m in memo:
                m = memo[m]

            if m == 1 or m == 89:
                cnt += m == 89
                for c in chain:
                    # record the end point for any number
                    # encountered in the chain
                    memo[c] = m

                break

            m = square_digit_sum(m)

    return cnt


if __name__ == "__main__":
    N = 10000000
    print(
        "Number of starting numbers below {} that arrive at 89: {}".format(
            N, square_digit_chains(N)
        )
    )
