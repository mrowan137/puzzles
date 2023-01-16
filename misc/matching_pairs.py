"""
Given two strings s and t of length N, find the maximum number of possible
matching pairs in strings s and t after swapping exactly two characters within
s. A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character
that is present at the ith and jth index of s, respectively. The matching pairs
of the two strings are defined as the number of indices for which s[i] and t[i]
are equal. Note: This means you must swap two characters at different indices.
"""
import math


def matching_pairs(s, t):
    # 1. understand the problem
    #    given two strings, find the maximum number of matching char,
    #    with the rule we MUST swap two chars in s
    #
    # 2. devise a plan
    #    a. brute force: consider all N^2 possible swap
    #       then count matches ~O(N^3)
    #    b. count base number of matches
    #       then check posible swaps, adjust the count
    #
    # 3. implement
    N = len(s)
    matchesWithoutSwap = sum(s[i] == t[i] for i in range(N))

    addFromSwap = float("-inf")
    for i in range(N):
        for j in range(i):
            addFromSwap = max(
                addFromSwap,
                int(s[i] == t[j])
                + int(s[j] == t[i])
                - int(s[i] == t[i])
                - int(s[j] == t[j]),
            )
            if addFromSwap == 2:
                return matchesWithoutSwap + addFromSwap

    return matchesWithoutSwap + addFromSwap

    # 4. check


# Tests we use to determine if the solution is correct.
def printInteger(n):
    print("[", n, "]", sep="", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(
            wrongTick, "Test #", test_case_number, ": Expected ", sep="", end=""
        )
        printInteger(expected)
        print(" Your output: ", end="")
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)
