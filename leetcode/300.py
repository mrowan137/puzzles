"""
Runtime: 4746 ms, faster than 11.12% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.5 MB, less than 75.92% of Python3 online submissions for Longest Increasing Subsequence.
"""
# O(N^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sz = len(nums)
        # max length of a subsequence ending at ith idx
        # choices: I can be a part of a subseq or not
        # case 1: I am part of subsequence;
        #         iterate through all candidate nums, taking
        #         pairwise max
        # case 2: I am not part of a subsequence;
        #         in other words, do nothing
        # dp[i] is the max subsequence ending in i
        dp = [1] * sz

        for i in range(1, sz):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


"""
Runtime: 3968 ms, faster than 34.22% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.6 MB, less than 47.20% of Python3 online submissions for Longest Increasing Subsequence.
"""
# key inight: each i can be the end of a subsequence, where nums[i]
# is the LARGEST element in the subsequence
# then the recursion is simple:
# dp[i] COULD BE dp[i-1] + 1 if nums[i] > nums[i-1]
# dp[i] COULD BE dp[i-2] + 1 if nums[i] > nums[i-2]
# ...
# and we should take the max of these possibilities for j in range(i)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        # dp[i] is the length of longest inreasing subsequence ending at i
        dp = [1] * N

        for i in range(1, N):
            for j in range(i):
                # this works, but too slow
                # dp[i] = max(dp[i],
                #            (dp[j] + int(nums[j] < nums[i]))*int(nums[j] < nums[i]))
                #
                # faster
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
