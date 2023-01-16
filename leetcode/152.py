"""
Runtime: 84 ms, faster than 19.80% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 14.6 MB, less than 29.28% of Python3 online submissions for Maximum Product Subarray.
"""
# O(N) save some memory
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sz = len(nums)
        big = sml = 1
        res = float("-inf")

        for n in nums:
            big_prev = big
            big = max(big * n, sml * n, n)
            sml = min(big_prev * n, sml * n, n)
            res = max(res, big)

        return res


"""
Runtime: 88 ms, faster than 14.09% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 15.8 MB, less than 6.66% of Python3 online submissions for Maximum Product Subarray.
"""
# O(N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # We use two arrays to track largest and smallest
        # product ending at an index. Positive number can generate
        # in two cases: +x+, -x-.  so we track the largest and smallest.
        # Without caring which case, we take the max, computing:
        # largest = max(smallest[i-1]*curr, # in case it is: -  *  -
        #                largest[i-1]*curr, # in case it is: +  *  +
        #                             curr) # in case it is: + or  -)
        # the last case can come about if largest[i-1] = smallest[i-1] = -
        # and curr is +. so we are agnostic about which case is realized,
        # and just take the max, which accounts for any of the cases
        sz = len(nums)
        big = [1] * sz
        sml = [1] * sz

        for i in range(sz):
            big[i] = max(big[i - 1] * nums[i], sml[i - 1] * nums[i], nums[i])
            sml[i] = min(big[i - 1] * nums[i], sml[i - 1] * nums[i], nums[i])

        return max(big)


"""
Runtime: 48 ms, faster than 96.12% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 15.7 MB, less than 7.40% of Python3 online submissions for Maximum Product Subarray.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        # dpp is max sum, dpn is min sum ending at i
        dpp, dpn = [0] * N, [0] * N

        # -inf emphasize there is no positive sum at i0 if n0 < 0
        # +inf emphasize there is no negative sum at i0 if n0 > 0
        dpp[0] = nums[0] if nums[0] >= 0 else -float("inf")
        dpn[0] = nums[0] if nums[0] < 0 else float("inf")

        for i in range(1, N):
            if nums[i] > 0:
                dpp[i] = max(dpp[i - 1] * nums[i], nums[i])
                dpn[i] = dpn[i - 1] * nums[i]
            elif nums[i] < 0:
                dpp[i] = dpn[i - 1] * nums[i]
                dpn[i] = min(dpp[i - 1] * nums[i], nums[i])

        return max(dpp)
