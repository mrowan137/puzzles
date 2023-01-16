"""
Runtime: 1672 ms, faster than 99.91% of Python3 online submissions for Dot Product of Two Sparse Vectors.
Memory Usage: 18.6 MB, less than 39.32% of Python3 online submissions for Dot Product of Two Sparse Vectors.
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        for i in range(vec.len):
            if vec.nums[i] != 0 and self.nums[i] != 0:
                res += vec.nums[i] * self.nums[i]

        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
