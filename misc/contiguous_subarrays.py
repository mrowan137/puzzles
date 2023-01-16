"""
Description:
  You are given an array arr of N integers. For each index i, you are required
  to determine the number of contiguous subarrays that fulfill the following
  conditions:
  * The value at index i must be the maximum element in the contiguous
  subarrays.
  * These contiguous subarrays must either start from or end on index i.

Signature:
  int[] countSubarrays(int[] arr)

Input:
  Array arr is a non-empty list of unique integers that range between 1 to
  1,000,000,000; size N is between 1 and 1,000,000.

Output:
  An array where each index i contains an integer denoting the maximum
  number of contiguous subarrays of arr[i].

Example:
  arr = [3, 4, 1, 6, 2]
  output = [1, 3, 1, 5, 1]
  Explanation:
  For index 0 - [3] is the only contiguous subarray that starts (or ends) with
    3, and the maximum value in this subarray is 3.
  For index 1 - [4], [3, 4], [4, 1]
  For index 2 - [1]
  For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
  For index 4 - [2]
  So, the answer for the above input is [1, 3, 1, 5, 1]
"""
import math

# optimize out max ~O(N^2): iterate over all possible subarrays,
#                           check if left is max (similar for right)
def count_subarrays(arr):
    N = len(arr)
    res = [1] * N

    # count right subarrays
    for i in range(N - 1):  # start
        m = arr[i]
        for j in range(i + 1, N):  # end
            m = max(m, arr[j])
            res[j] += arr[j] == m

    # count left subarrays
    for i in range(N - 1, -1, -1):  # start
        m = arr[i]
        for j in range(i - 1, -1, -1):  # end
            m = max(m, arr[j])
            res[j] += arr[j] == m

    return res


# brute force ~O(N^3): iterate over all possible subarrays,
#                      check if left is max (similar for right)
"""
def count_subarray(arr):
    N = len(arr)
    res = [1]*N

    # iterate over subarrays of size more than 2; i and j is the valid idx
    for i in range(N-1): # start
        for j in range(i+1, N): # end
            res[i] += arr[i] == max(arr[i:j+1])
            res[j] += arr[j] == max(arr[i:j+1])

    return res
"""

# Tests to determine if the solution is correct.
def printInteger(n):
    print("[", n, "]", sep="", end="")


def printIntegerList(array):
    size = len(array)
    print("[", end="")
    for i in range(size):
        if i != 0:
            print(", ", end="")
        print(array[i], end="")
    print("]", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= output[i] == expected[i]
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(
            wrongTick, "Test #", test_case_number, ": Expected ", sep="", end=""
        )
        printIntegerList(expected)
        print(" Your output: ", end="")
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    test_1 = [3, 4, 1, 6, 2]
    expected_1 = [1, 3, 1, 5, 1]
    output_1 = count_subarrays(test_1)
    check(expected_1, output_1)

    test_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [1, 2, 6, 1, 3, 1]
    output_2 = count_subarrays(test_2)
    check(expected_2, output_2)
