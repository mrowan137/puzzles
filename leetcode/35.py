"""
Runtime: 81 ms, faster than 14.65% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.1 MB, less than 22.57% of Python3 online submissions for Search Insert Position.
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l
