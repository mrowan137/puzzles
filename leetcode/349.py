"""
Runtime: 59 ms, faster than 38.36% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.4 MB, less than 47.96% of Python3 online submissions for Intersection of Two Arrays.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # n log n
        nums2.sort()  # m log m

        i = j = 0

        res = []
        while i < len(nums1) and j < len(nums2):  # O(min(m, n))
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                while i < len(nums1) and nums1[i] == res[-1]:
                    i += 1
                while j < len(nums2) and nums2[j] == res[-1]:
                    j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return res


"""
Runtime: 40 ms, faster than 92.60% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.3 MB, less than 76.78% of Python3 online submissions for Intersection of Two Arrays.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        # nums1 is the shorter of nums1, nums2

        nums2 = set(nums2)  # O(m) to convert
        res = set()  # intersection of nums1, nums2

        for n in nums1:  # ~O(n)
            if n in nums2 and n not in res:  # ~O(1) contains op
                res.add(n)

        # O(n+m) altogether to convert nums2 and iterate nums1

        return [x for x in res]
