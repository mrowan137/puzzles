class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Simple case
        # [1 2]
        # [1 2]
        # 1 + 4 = 5 [1, 2] x [2, 1]
        # 2 + 2 = 4
        # [1, 2, 3]
        # [1, 2, 3]
        # 1 + 4 + 9 = 14
        # [1, 2, 3] x [1, 2, 3] = 14
        # [1, 2, 3] x [1, 3, 2] = 13
        # [1, 2, 3] x [2, 3, 1] = 11
        # [1, 2, 3] x [2, 1, 3] = 13
        # [1, 2, 3] x [3, 1, 2] = 11
        # [1, 2, 3] x [3, 2, 1] = 10 --> winner
        # Idea: match sorted asc. to sorted desc
        """
        Runtime: 1180 ms, faster than 35.27% of Python3 online submissions for Minimize Product Sum of Two Arrays.
        Memory Usage: 24.1 MB, less than 6.04% of Python3 online submissions for Minimize Product Sum of Two Arrays.
        """
        # nums1 = sorted(nums1)
        # nums2 = sorted(nums2)[::-1]
        # return sum([nums1[i]*nums2[i] for i in range(len(nums1))])

        # Now make use of fact 1 <= nums1[i] <= 100
        """
        Runtime: 1204 ms, faster than 32.37% of Python3 online submissions for Minimize Product Sum of Two Arrays.
        Memory Usage: 19.3 MB, less than 33.33% of Python3 online submissions for Minimize Product Sum of Two Arrays.
        """
        sz = 101
        nums1_count = [0] * sz
        nums2_count = [0] * sz
        for i in range(len(nums1)):
            nums1_count[nums1[i]] += 1
            nums2_count[nums2[i]] += 1

        m, n, res = 0, sz - 1, 0
        while m < sz and n >= 0:
            if nums1_count[m] and nums2_count[n]:
                res += m * n
                nums1_count[m] -= 1
                nums2_count[n] -= 1

            if not nums1_count[m]:
                m += 1
            if not nums2_count[n]:
                n -= 1

        return res
