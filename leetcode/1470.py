"""
Runtime: 88 ms, faster than 58.66% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.2 MB, less than 40.58% of Python3 online submissions for Shuffle the Array.
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # big brain solutions: encode x1 ... xn into the 2nd half of array
        for i in range(n, 2 * n):
            nums[i] = nums[i] * 1001 + nums[i - n]

        # nums[i] % 1000 = x, nums[i] // 1000 = y
        idx = n
        for i in range(0, 2 * n, 2):
            nums[i] = nums[idx] % 1001
            nums[i + 1] = nums[idx] // 1001
            idx += 1

        return nums


"""
Runtime: 60 ms, faster than 75.29% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.3 MB, less than 93.07% of Python3 online submissions for Shuffle the Array.
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1, nums2 = nums[:n], nums[n:]

        res = []
        for p in zip(nums1, nums2):
            res.append(p[0])
            res.append(p[1])

        return res
