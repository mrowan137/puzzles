"""
Runtime: 248 ms, faster than 34.40% of Python3 online submissions for Binary Search.
Memory Usage: 15.4 MB, less than 91.62% of Python3 online submissions for Binary Search.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m

        return -1
