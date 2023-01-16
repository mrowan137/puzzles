"""
Runtime: 512 ms, faster than 85.48% of Python3 online submissions for Maximum Sum Circular Subarray.
Memory Usage: 18.6 MB, less than 26.36% of Python3 online submissions for Maximum Sum Circular Subarray.

compute the max and min subarrays that do not wrap around
either the max arrays is largest, or the sum minus min is largest
either way, one of those is the maximum wrapping around subarray
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sz = len(nums)
        dpmax, dpmin = [float("-inf")] * sz, [float("inf")] * sz
        for i in range(sz):
            dpmax[i] = max(dpmax[i - 1] + nums[i], nums[i])
            dpmin[i] = min(dpmin[i - 1] + nums[i], nums[i])

        # edge case, if min subarray takes all the nums
        # so that max wrap around subarray contains nothing
        if all(n <= 0 for n in nums):
            return max(nums)

        # now we know min subarray does not contain all nums
        return max([max(dpmax), sum(nums) - min(dpmin)])


"""
Runtime: 488 ms, faster than 88.56% of Python3 online submissions for Maximum Sum Circular Subarray.
Memory Usage: 18.5 MB, less than 34.18% of Python3 online submissions for Maximum Sum Circular Subarray.

there's just 2 cases:
1. the max subarray split over begin, end
2. the min subarray split over begin, end
so we can compute max, min subarrs
and take whatever is the larger
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # this is for edge case; max subarray
        # must contain at least one element
        if all(x < 0 for x in nums):
            return max(nums)

        sz = len(nums)
        s = sum(nums)

        # compute max subarray
        dp = [float("-inf")] * sz
        dp[0] = nums[0]
        for i in range(1, sz):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        mx = max(dp)

        # compute min subarray
        dp[0] = nums[0]
        for i in range(1, sz):
            dp[i] = min(dp[i - 1] + nums[i], nums[i])
        mn = min(dp)

        return max(s - mn, mx)


"""
Runtime: 524 ms, faster than 71.27% of Python3 online submissions for Maximum Sum Circular Subarray.
Memory Usage: 18.6 MB, less than 38.30% of Python3 online submissions for Maximum Sum Circular Subarray.

Symmetry
Think: we know how to solve the 'max subarray' problem
How could we use that to create a strategy?
If subarray doesn't map around, it's just the problem we know
If it wraps around, how can we use that info?  In that case,
the min subarray does not wrap around, and we can solve for
that using the same method, then use it to deduce the max subarray.
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = min_sum = max_sum = curr_max = curr_min = 0
        for n in nums:
            curr_min = min(n + curr_min, n)
            min_sum = min(min_sum, curr_min)
            curr_max = max(n + curr_max, n)
            max_sum = max(max_sum, curr_max)
            total += n

        return (
            max(total - min_sum, max_sum)
            if any(n > 0 for n in nums) > 0
            else max(nums)
        )


"""
TLE
"""
# O(N^2)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums += nums
        N = len(nums)

        # dp[i][k] is the max sum that ends in entry i and extends over at most k+1 entries
        # dp[i][k] = max(dp[i-1][k-1] + nums[i], nums[i])
        dp = [[-float("inf")] * (N // 2) for _ in range(N)]

        # iterate
        for i in range(N):
            dp[i][: min(i, N // 2)] = [
                max(dp[i - 1][k - 1] + nums[i], nums[i])
                for k in range(min(i, N // 2))
            ]
        return max(dp[i][-1] for i in range(N))
