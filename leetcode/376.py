"""
Runtime: 32 ms, faster than 81.60% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 14.2 MB, less than 67.46% of Python3 online submissions for Wiggle Subsequence.
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        sz = len(nums)
        dpp = [1] * sz
        dpn = [1] * sz

        for i in range(1, sz):
            if nums[i] - nums[i - 1] > 0:
                dpp[i] = max(
                    1 + dpn[i - 1], dpp[i - 1]  # using current num
                )  # deleting current num
                dpn[i] = dpn[i - 1]
            elif nums[i] - nums[i - 1] < 0:
                dpn[i] = max(
                    1 + dpp[i - 1], dpn[i - 1]  # using current num
                )  # deleting current num
                dpp[i] = dpp[i - 1]
            else:
                dpp[i] = dpp[i - 1]  # zero wiggle must be delete
                dpn[i] = dpn[i - 1]

        return max(max(dpp), max(dpn))


"""
Runtime: 196 ms, faster than 16.37% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 14.4 MB, less than 38.48% of Python3 online submissions for Wiggle Subsequence.
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)

        # dp[i] represents length of longest wiggle subsequence
        # ending on a down (dpn) or an up (dpp)
        # initial condition:
        dpp = [1] * N
        dpn = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[i] - nums[j] > 0:
                    dpp[i] = max(dpp[i], dpn[j] + 1)
                elif nums[i] - nums[j] < 0:
                    dpn[i] = max(dpn[i], dpp[j] + 1)

        return max(max(dpp), max(dpn))
