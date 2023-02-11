"""
Q: The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

  F1 = 1
  F2 = 1
  F3 = 2
  F4 = 3
  F5 = 5
  F6 = 8
  F7 = 13
  F8 = 21
  F9 = 34
  F10 = 55
  F11 = 89
  F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?

A: 4782
"""


def longhand_add(num1, num2):
    sz1, sz2 = len(num1), len(num2)
    res = []

    place = 0
    carry = 0

    while place < min(sz1, sz2):
        carry += num1[sz1 - 1 - place] + num2[sz2 - 1 - place]

        digit, carry = carry % 10, carry // 10
        res = [digit] + res
        place += 1

    # add remaining digits of carry to the larger number and append to result
    num = num1 if sz1 > sz2 else num2
    sz = sz1 if sz1 > sz2 else sz2

    while place < max(sz1, sz2):
        carry += num[sz - 1 - place]

        digit, carry = carry % 10, carry // 10
        res = [digit] + res
        place += 1

    # add any remaining digits from carry
    while carry:
        digit, carry = carry % 10, carry // 10
        res.insert(0, digit)

    return res


def idx_of_fib_term_with_n_digits(n):
    a, b = [1], [1]
    idx = 2

    # by assumption, there is a term with 1000 digits
    # so this terminates for n = 1000
    while len(b) != n:
        b, a = longhand_add(a, b), b
        idx += 1

    return idx


if __name__ == "__main__":
    N = 1000
    print(
        "Index of first Fibonacci term with {} digits: {}".format(
            N, idx_of_fib_term_with_n_digits(N)
        )
    )
