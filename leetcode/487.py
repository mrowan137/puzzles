"""
Runtime: 440 ms, faster than 20.62% of Python3 online submissions for Max Consecutive Ones II.
Memory Usage: 14.5 MB, less than 22.26% of Python3 online submissions for Max Consecutive Ones II.
"""
# O(n) sliding window, using less memory
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window, tracking number of zeros
        # we saw so far.  if we saw 2, we need to shrink until
        # the window is valid
        l = r = 0
        num_zeros = 0
        res = 0

        # invariant: [l, r] windows a sequence with no more than
        # a single zero somewhere in between
        while r < len(nums):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros == 2:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res


"""
Runtime: 400 ms, faster than 62.18% of Python3 online submissions for Max Consecutive Ones II.
Memory Usage: 15.1 MB, less than 6.12% of Python3 online submissions for Max Consecutive Ones II.
"""
# O(n) dp
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # dp[j][i] = max number of consecutive ones
        # ending at idx i given you already flipped j bits
        # the choice we can make is flip or not flip a zero bit
        sz = len(nums)
        dp = [[0] * sz for _ in range(2)]

        for i in range(sz):
            if nums[i] == 0:
                dp[0][i] = 0  # don't flip, restart at 0
                dp[1][i] = dp[0][i - 1] + 1  # flip the zero
            elif nums[i] == 1:
                dp[0][i] = dp[0][i - 1] + 1  # add 1 to sequence
                dp[1][i] = dp[1][i - 1] + 1  # add 1 to sequence

        return max(max(row) for row in dp)
