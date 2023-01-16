"""
Runtime: 417 ms, faster than 21.73% of Python3 online submissions for Uncrossed Lines.
Memory Usage: 14.8 MB, less than 32.39% of Python3 online submissions for Uncrossed Lines.
"""


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        sz1, sz2 = len(nums1), len(nums2)
        dp = [[0] * (sz1 + 1) for _ in range(sz2 + 1)]
        for j in range(1, sz2 + 1):
            for i in range(1, sz1 + 1):
                # cases: 1. join matching nums, then max num crossing lines
                #        is matches(nums1[:i-1], nums2[:j-1]) + 1
                #        2. don't join; then the max num crossing lines
                #        including the current letter is greater of the
                #        cases excluding either ith of nums1 or jth of nums2
                #        "if those two don't match, drop one of 'em and take
                #         the max num crossings from either case.. don't drop
                #         both because one or the other might connect to thing!"
                dp[j][i] = max(
                    dp[j - 1][i - 1] + int(nums1[i - 1] == nums2[j - 1]),
                    dp[j - 1][i],
                    dp[j][i - 1],
                )

        return max(max(row) for row in dp)
