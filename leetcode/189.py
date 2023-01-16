"""
Runtime: 289 ms, faster than 30.80% of Python3 online submissions for Rotate Array.
Memory Usage: 25.4 MB, less than 83.76% of Python3 online submissions for Rotate Array.
"""
# O(1) memory, separating replacements into modulo classes to treat independently
# Why does this work?  Well, for the different modulo classes we know 2 things
# 1. the indiviual modulo classes will not interfere with another (so can be
#    treated independently)
# 2. for an individual modulo class, the elements replace as
#    n--> 1 --> 2 --> 3,..., --> n, and we need just O(1)
# For concrete example, consider [1,2,3,4,5,6,7] an a rotation of 2
# List out the modulo classes:
# [1 2 3 4 5 6 7] --> [7   1   3   5] --> [7   1   3   5] --> [7 6 1 2 3 4 5]
#                     [  2   4   6  ] --> [  6   2   4  ]
# [0 1 0 1 0 1 0]     [0 1 0 1 0 1 0] --> [0 1 0 1 0 1 0]
#
# This works because we take each element and push it into the correct
# position, taking out the displaced one to put directly into the correct
# position.  This swapping does not work if we just put 1 in place, then
# put 2 in place, because we hold the 3 and the 4 and it's not longer O(1)
# space.  Instead, the strategy is motivated by the thinking "let's put 1
# in place, and pop out the 3.  Now could we put the 3 in places?"  The answer
# is yes if we cycle according to the modulo classes.
# When current index is start, increment start by 1 and cycle the next modulo class.
# Continue as long as the number of placed elements is less than the number of nums.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Could also O(1) space, cylical shift using modulo class
        """
        N = len(nums)
        k %= N

        placed = 0
        start = curr = 0
        n_prev = nums[start]
        while placed < N:
            # iterate
            curr = (curr + k) % N

            # store curr
            n_curr = nums[curr]

            # place prev into curr
            nums[curr] = n_prev
            placed += 1

            # make curr into prev
            n_prev = n_curr

            if curr == start and start < len(nums) - 1:
                start = start + 1
                n_prev = nums[start]
                curr = start


"""
Runtime: 339 ms, faster than 31.50% of Python3 online submissions for Rotate Array.
Memory Usage: 25.5 MB, less than 55.18% of Python3 online submissions for Rotate Array.
"""
# Another attempt, rotation
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        placed = 0
        k %= N

        i_orig = i = 0
        out1 = nums[i]
        while placed < N:
            i = (i + k) % N

            # swap
            out2 = nums[i]
            nums[i] = out1
            out1 = out2

            placed += 1

            # place things in the mod class
            if (i + k) % N == i_orig and i_orig < N - 1:
                nums[i_orig] = out1
                i_orig += 1
                i = i_orig
                out1 = nums[i]
                placed += 1


"""
Runtime: 427 ms, faster than 19.72% of Python3 online submissions for Rotate Array.
Memory Usage: 25.7 MB, less than 13.46% of Python3 online submissions for Rotate Array.
"""
# using extra memory, O(N*2) for res and copy of nums
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        numsnums = nums + nums

        res = []
        for i in range(N):
            res.append(numsnums[N - k + i])

        for i in range(N):
            nums[i] = res[i]


"""
Runtime: 232 ms, faster than 48.62% of Python3 online submissions for Rotate Array.
Memory Usage: 25.5 MB, less than 83.98% of Python3 online submissions for Rotate Array.
"""
# reverse O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        O(1) space: save the last element, shift the rest to the right
        """

        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        N = len(nums)
        k %= N

        reverse(nums, 0, N - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, N - 1)


"""
TLE
"""
# Brute force
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        O(1) space: save the last element, shift the rest to the right
        """
        N = len(nums)
        k %= N
        for i in range(k):
            last = nums[-1]
            for i in range(N - 1):
                nums[N - i - 1] = nums[N - i - 2]
            nums[0] = last
