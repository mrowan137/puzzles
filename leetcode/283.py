"""
Runtime: 164 ms, faster than 42.76% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 25.60% of Python3 online submissions for Move Zeroes.
"""
# Another rewrite
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        write = 0  # location of the first zero
        while write < N and nums[write] != 0:
            write += 1

        read = write + 1

        while read < N:
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

            read += 1

        while write < N:
            nums[write] = 0
            write += 1


"""
Runtime: 168 ms, faster than 16.94% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 88.08% of Python3 online submissions for Move Zeroes.
"""
# More recent rewrite
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)

        write = 0
        for n in nums:
            if n != 0:
                nums[write] = n
                write += 1

        # Overwrite last with zeros
        nums[write:] = [0] * len(nums[write:])


"""
Runtime: 52 ms, faster than 48.62% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 16.89% of Python3 online submissions for Move Zeroes.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first zero
        fz = 0
        while fz < len(nums):
            if nums[fz] == 0:
                break
            fz += 1

        if fz == len(nums):
            return

        # j and i are at the first zero
        j = fz
        for i in range(fz, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
