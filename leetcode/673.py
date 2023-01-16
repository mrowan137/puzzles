"""
Runtime: 1065 ms, faster than 85.28% of Python3 online submissions for Number of Longest Increasing Subsequence.
Memory Usage: 14.4 MB, less than 85.42% of Python3 online submissions for Number of Longest Increasing Subsequence.
"""
# O(N^2)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        sz = len(nums)

        dp = [1] * sz  # length of longest increasing subseq ending at i
        l = [1] * sz  # number of longest increasing subseq ending at i

        for i in range(1, sz):
            for j in range(i):
                if nums[j] < nums[i]:
                    # an inc subsequence ends here
                    candidate_max, curr_max = dp[j] + 1, dp[i]

                    if candidate_max > curr_max:
                        # there is a new max length of longest inc subseq
                        dp[i] = candidate_max

                        # the number of longest inc subseq ending at i
                        # is the number of longet inc subseq ening at j
                        l[i] = l[j]
                    elif candidate_max == curr_max:
                        # there is another longest inc subseq of equal length
                        # to something alreay found, so add these to the count
                        l[i] += l[j]

        # count sequences with the max length
        m = max(dp)
        res = 0
        for i in range(sz):
            if dp[i] == m:
                res += l[i]

        return res
