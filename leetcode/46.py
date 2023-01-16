"""
Runtime: 40 ms, faster than 70.00% of Python3 online submissions for Permutations.
Memory Usage: 14.3 MB, less than 69.27% of Python3 online submissions for Permutations.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        # choose 1 to the front, permute the rest
        res = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i + 1 :]):
                res.append([nums[i]] + p)

        return res
