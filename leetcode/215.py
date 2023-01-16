"""
Runtime: 68 ms, faster than 45.47% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.2 MB, less than 43.58% of Python3 online submissions for Kth Largest Element in an Array.
"""
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # make a max heap
        # heap has the heap property: children key are <= parent key
        # complexity:
        #   - build the heap: O(n) (shorter than to sort)
        #   - pop: O(log(n))
        nums_inv = [-n for n in nums]
        heapq.heapify(nums_inv)
        for _ in range(k - 1):
            heapq.heappop(nums_inv)
        return -1 * min(nums_inv)


"""
Runtime: 1124 ms, faster than 10.75% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 116.9 MB, less than 5.23% of Python3 online submissions for Kth Largest Element in an Array.
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # idea: recursion
        # remove the max, then find k-1 largest in remaining list
        # could also use heapq an pop k times largest of the list
        if k == 1:
            return max(nums)

        i = nums.index(max(nums))
        return self.findKthLargest(nums[:i] + nums[i + 1 :], k - 1)
