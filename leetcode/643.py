"""
Runtime: 1401 ms, faster than 83.66% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 26.3 MB, less than 19.06% of Python3 online submissions for Maximum Average Subarray I.
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)

        # 2 pointers
        i, j = 0, k
        res = avg = sum(nums[0:k]) / k
        while j < len(nums):
            avg += (nums[j] - nums[i]) / k
            i += 1
            j += 1
            res = max(res, avg)

        return res
