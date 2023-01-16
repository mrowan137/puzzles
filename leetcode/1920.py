"""
Runtime: 140 ms, faster than 60.20% of Python3 online submissions for Build Array from Permutation.
Memory Usage: 14.3 MB, less than 69.94% of Python3 online submissions for Build Array from Permutation.
"""
# O(N) time, O(1) space
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # it would be nice if we can takes
        # nums = [a, b, c]
        #    --> [(a, nums[a]), (b, nums[b]), (c, nums[c])]
        #    --> [nums[a], nums[b], nums[c]]
        # so we do not overwrite the crucial information
        # when filling out nums in place. e.g.,
        # nums = [1, 0]
        # nums[0] = nums[nums[0]] = 0
        # nums[1] = nums[nums[1]] = 0 (! meant to be 1)
        # would get messed up because we overwrote nums[0]
        #
        # we could retain the information with an encoding,
        # a = b*q + r; let r = nums[i], b = nums[nums[i]]
        # where r < q.  then a // q = b, and a % q = r.
        # so the steps:
        # 1. encode nums to a = b*q+r
        #        - note if it was not yet encoded, a, b of above are 0
        # 2. decode by extract the b value
        # since the r value are indices, 0 <= i <= len(nums) - 1,
        # q can be the length of the array
        q = len(nums)

        # encode nums_encoded[i] = b*q + r, where r = nums[i]
        # of the original array, and b = nums[nums[i]].
        # note that nums[i]%q = nums_encoded[i]%q, we get the original
        # nums array by mod q.
        for i in range(q):
            r = nums[i] % q
            b = nums[nums[i]] % q
            nums[i] = b * q + r

        for i in range(q):
            nums[i] = nums[i] // q

        return nums


"""
Runtime: 124 ms, faster than 62.49% of Python3 online submissions for Build Array from Permutation.
Memory Usage: 14.5 MB, less than 40.77% of Python3 online submissions for Build Array from Permutation.
"""


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
