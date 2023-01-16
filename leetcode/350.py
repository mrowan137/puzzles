"""
Runtime: 44 ms, faster than 82.93% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.5 MB, less than 38.31% of Python3 online submissions for Intersection of Two Arrays II.
"""
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 is the longer of the two lists
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)

        # hashmaps
        cnt1, cnt2 = Counter(nums1), Counter(nums2)

        # iterate through the shorter list
        res = []
        for n in nums2:
            if n in cnt1.keys() and n in cnt2.keys() and cnt1[n] and cnt2[n]:
                cnt1[n] -= 1
                cnt2[n] -= 1
                res.append(n)

        return res
