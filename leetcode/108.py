"""
Runtime: 60 ms, faster than 62.41% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.7 MB, less than 59.69% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 2:
            root = TreeNode(max(nums))
            root.left = TreeNode(min(nums))
            return root

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root
