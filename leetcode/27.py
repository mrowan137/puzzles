"""
Runtime: 36 ms, faster than 51.96% of Python3 online submissions for Remove Element.
Memory Usage: 14.3 MB, less than 49.32% of Python3 online submissions for Remove Element.
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i, j, sz = 0, 0, len(nums)

        while i < sz and nums[i] != val:
            i += 1
        j = i + 1

        while i < sz and j < sz:
            if nums[j] != val:
                nums[i] = nums[j]
                nums[j] = val
                while i < sz and nums[i] != val:
                    i += 1

            j += 1

        return i
