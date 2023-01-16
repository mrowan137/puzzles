"""
Runtime: 28 ms, faster than 95.86% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.1 MB, less than 75.43% of Python3 online submissions for First Missing Positive.

Note the smallest positive is in [1, 2, ..., sz + 1] where sz is the length of nums.
So we can store at the index in nums whether that index was seen, via a hash function,
without obfuscating the value stored at that index.
1. Remove values outside the possible range (<1 or >sz+1) then store whether value
2. Add a value at the beginning to deposit when useless value is seen

O(N) time complexity, constant memory
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sz = len(nums)

        # Remove values outside valid range
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > sz + 1:
                nums[i] = 0

        # values at indices 1, ..., sz store whether those values (1, ..., sz) were seen
        # add bin at the beginning for useless values incrementation
        # add bin at the end to capture all [1, sz+1] possible values
        # hash will be sz+2 since all possible values % sz+2  == value
        nums = [0] + nums + [0]
        for i in range(1, len(nums)):
            nums[nums[i] % (sz + 2)] += sz + 2
        for i in range(1, len(nums)):
            if nums[i] // (sz + 2) == 0:
                return i


"""
Runtime: 28 ms, faster than 95.86% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.1 MB, less than 75.43% of Python3 online submissions for First Missing Positive.

Complexity analysis:
    - O(NlogN) to construct heap then pop root
"""
import heapq


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        while nums and nums[0] < 1:
            heapq.heappop(nums)

        if not nums:
            return 1
        if nums[0] != 1:
            return 1

        while nums:
            curr = heapq.heappop(nums)
            peek = None if not nums else nums[0]
            if peek and curr + 1 != peek and curr != peek:
                return curr + 1

        return curr + 1


"""
Runtime: 36 ms, faster than 59.15% of Python3 online submissions for First Missing Positive.
Memory Usage: 14 MB, less than 98.49% of Python3 online submissions for First Missing Positive.

O(NlogN) sorting
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        while nums and nums[0] < 1:
            nums.pop(0)

        if not nums:
            return 1
        if nums[0] != 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1] and nums[i] != nums[i + 1]:
                return nums[i] + 1

        return nums[-1] + 1
