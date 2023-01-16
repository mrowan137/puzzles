"""
Runtime: 484 ms, faster than 19.91% of Python3 online submissions for Largest Divisible Subset.
Memory Usage: 14.7 MB, less than 26.70% of Python3 online submissions for Largest Divisible Subset.
"""
# O(N^2) dp
class Solution(object):
    def largestDivisibleSubset(self, nums):
        sz = len(nums)
        if sz == 0:
            return []

        # we will use the mathematical observation, that if largest in the subset
        # divides candidate, all smaller nums in the subset divide the candidate
        # which allows us to build the subset 1 num at a time, given sorted list
        nums.sort()

        # dp[i] is the max subset size considering up to i, and including i
        dp = [0] * (len(nums))

        # Compute the largest subset up to ith num; for a given i,
        # iterate through nums, checking if jth divides current largest (i.e., ith)
        # If it does, subset ending at jth, in combination with ith, is new largest
        # And note that if largest (jth) in the subset divides larger (ith), all
        # smaller numbers in the subset also divide the ith
        for i in range(sz):
            max_subset_size = 0
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    max_subset_size = max(max_subset_size, dp[j])

            max_subset_size += 1
            dp[i] = max_subset_size

        # get size and index of max subset size
        max_subset_size, i_max = max([(s, i) for i, s in enumerate(dp)])

        # build the largest subset, iterating backwards
        res = []
        curr_size = max_subset_size
        j = i_max
        while curr_size > 0 and j >= 0:
            if dp[j] == curr_size and nums[i_max] % nums[j] == 0:
                res = [nums[j]] + res
                curr_size -= 1
                i_max = j

            j -= 1

        return res
