"""
Runtime: 48 ms, faster than 74.64% of Python3 online submissions for Find Peak Element.
Memory Usage: 14 MB, less than 88.25% of Python3 online submissions for Find Peak Element.
"""
# O(log2n), recursion
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # note nums[i] != nums[i+1] for all i; no neighbors are equal
        # so what are the patterns?
        # 1 2 3 --> search on the right
        # 3 2 1 --> search on the left
        # 1 2 1 --> found a peak
        # 3 2 3 --> we can search either side
        #           (but really, it should be shown rigorously)
        def recurse(nums, l, r):
            m = (l + r) // 2
            if m - 1 >= 0:
                a = nums[m - 1]
            else:
                a = float("-inf")
            if m + 1 <= len(nums) - 1:
                c = nums[m + 1]
            else:
                c = float("-inf")

            if a < nums[m] and nums[m] > c:
                return m
            elif a < nums[m] and nums[m] < c:
                return recurse(nums, m + 1, r)
            else:
                return recurse(nums, l, m - 1)

        return recurse(nums, 0, len(nums) - 1)


"""
Runtime: 65 ms, faster than 43.60% of Python3 online submissions for Find Peak Element.
Memory Usage: 14.1 MB, less than 77.96% of Python3 online submissions for Find Peak Element.
"""
# O(log2n), iteration
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # note nums[i] != nums[i+1] for all i; no neighbors are equal
        # so what are the patterns?
        # 1 2 3 --> search on the right
        # 3 2 1 --> search on the left
        # 1 2 1 --> found a peak
        # 3 2 3 --> we can search either side
        #           (but really, it should be shown rigorously)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if m - 1 >= 0:
                a = nums[m - 1]
            else:
                a = float("-inf")
            if m + 1 <= len(nums) - 1:
                c = nums[m + 1]
            else:
                c = float("-inf")
            b = nums[m]

            if a < b and b > c:
                return m
            elif a < b and b < c:
                l = m + 1
            else:
                r = m - 1

        return m
