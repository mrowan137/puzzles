"""
Runtime: 125 ms, faster than 30.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 46.34% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
# Two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0

        # continue while j in bounds
        while j < len(nums):
            # after this, have i, j s.t. nums[i] != nums[j]
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            # above loop is possible j goes out of bounds
            # like [1,1]; we're done so exit in this case
            if j > len(nums) - 1:
                break

            # swap nums[j] into place
            nums[i + 1], nums[j] = nums[j], nums[i + 1]

            i += 1
            j += 1

        return i + 1


"""
Runtime: 3798 ms, faster than 5.01% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 7.05% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
# Brute force
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i:] = nums[i + 1 :]
                i -= 1
            i += 1

        return len(nums)
