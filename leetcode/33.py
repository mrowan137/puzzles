"""
Runtime: 44 ms, faster than 38.67% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.8 MB, less than 22.60% of Python3 online submissions for Search in Rotated Sorted Array.
"""
# O(logN) since using binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        # identify the pivot index
        def find_rot_ind(l, r):
            if nums[l] < nums[r]:
                return 0  # the array is already sorted

            while l <= r:
                m = (l + r) // 2

                if nums[m] > nums[m + 1]:
                    return m + 1
                elif nums[m] < nums[0]:
                    r = m - 1
                elif nums[m] >= nums[0]:
                    l = m + 1

        # rotate back
        shift = find_rot_ind(0, len(nums) - 1)
        nums = nums[shift:] + nums[:shift]

        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return (m + shift) % len(nums)
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return -1
