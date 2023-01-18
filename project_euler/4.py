"""
Q: A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
palindrome made from the product of two 3-digit numbers.
 
A: 906609
"""


def is_palindrome(x):
    i, j = 0, len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False

        i += 1
        j -= 1

    return True


def largest_palindrome_number():
    # consider combinations of two 3-digit numbers and
    # take the largest one that is palindrome;
    # there's less than 1000*1000 possibilities to check
    nums = [
        str(x) + str(y) + str(z)
        for x in range(1, 10)
        for y in range(10)
        for z in range(10)
    ]

    res = float("-inf")
    for n1 in nums:
        for n2 in nums:
            product = int(n1) * int(n2)
            res = max(res, product) if is_palindrome(str(product)) else res

    return res


if __name__ == "__main__":
    print(
        "Largest palindrome made from product of two 3-digit numbers: {}".format(
            largest_palindrome_number()
        )
    )
