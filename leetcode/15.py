"""
Runtime: 1548 ms, faster than 37.59% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 86.91% of Python3 online submissions for 3Sum.
"""


class Solution:
    def twoSum(self, target, nums):
        # find two nums that sum to a target
        # return the nums if present
        # the nums cannot be the same!

        # if m = target-n, then m + n == target
        # m value --> index of pair n
        dic = {target - n: i for i, n in enumerate(nums)}
        res = []

        for i, n in enumerate(nums[:-1]):
            # skip if we already did this
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # append if correct sum and past current index
            if n in dic.keys() and i < dic[n]:
                res.append([n, nums[dic[n]]])

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # search for two other nums in the list that sum to -n
        for i, n in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # check for valid pairs and append
            candidate = self.twoSum(-n, nums[i + 1 :])
            for c in candidate:
                res.append([n] + c)

        return res


# TLE
class Solution:
    def twoSum(self, target, nums):
        # find two nums that sum to a target
        # return the nums if present
        # the nums cannot be the same!

        # if m = target-n, then m + n == target
        # m value --> index of pair n
        dic = {target - n: i for i, n in enumerate(nums)}

        res = []
        # for i,n in enumerate(nums):
        #    if n in dic.keys() and i != dic[n]:
        #        res.append([n, nums[dic[n]]])

        # return res

        return [
            [n, nums[dic[n]]]
            for i, n in enumerate(nums)
            if n in dic.keys() and i != dic[n]
        ]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        # search for two other nums in the list that sum to -n
        for i, n in enumerate(nums):
            candidate = self.twoSum(-n, nums[:i] + nums[i + 1 :])
            if candidate:
                triplet = [[n] + list(c) for c in candidate]
                for t in triplet:
                    t_str = "".join([str(num) + " " for num in sorted(t)])
                    if t_str not in seen:
                        seen.add(t_str)
                        res.append(t)

        return res
