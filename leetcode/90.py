"""
Runtime: 79 ms, faster than 14.18% of Python3 online submissions for Subsets II.
Memory Usage: 14.2 MB, less than 9.41% of Python3 online submissions for Subsets II.
"""


class Solution:
    def dfs(self, i, curr, res, nums):
        res.append(curr)
        j = i
        while j < len(nums):
            while (j > i) and (j < len(nums)) and (nums[j] == nums[j - 1]):
                j += 1
            if j >= len(nums):
                return
            self.dfs(j + 1, curr + [nums[j]], res, [n for n in nums])
            j += 1

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # first argument is the index of nums from
        # which to consider building a subset
        self.dfs(0, [], res, nums)
        return res
