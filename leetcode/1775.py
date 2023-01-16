"""
Runtime: 1859 ms, faster than 42.46% of Python3 online submissions for Equal Sum Arrays With Minimum Number of Operations.
Memory Usage: 18.1 MB, less than 98.61% of Python3 online submissions for Equal Sum Arrays With Minimum Number of Operations.
"""
# O(N)
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums1) > sum(nums2):
            return self.minOperations(nums2, nums1)
        nums1.sort()
        nums2.sort()
        i, j = 0, len(nums2) - 1

        # while there's still hope,
        s1, s2 = sum(nums1), sum(nums2)
        res = 0
        while (i < len(nums1) and j >= 0) and s1 < s2:
            # early exit
            if nums1[i] == 6 and nums2[j] == 1:
                return -1

            # add whichever one get us the closer
            if (i == len(nums1) and j >= 0) or (nums2[j] >= 7 - nums1[i]):
                s2 -= nums2[j] - 1  # nums2[j] = 1
                j -= 1
            else:
                s1 += 6 - nums1[i]  # nums1[i] = 6
                i += 1

            res += 1

        # there can be leftovers
        while i < len(nums1) and s1 < s2 and nums1[i] != 6:
            s1 += 6 - nums1[i]
            i += 1
            res += 1
        while j >= 0 and s1 < s2 and nums2[j] != 1:
            s2 -= nums2[j] - 1
            j -= 1
            res += 1

        return res if s1 >= s2 else -1
