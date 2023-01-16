"""
Runtime: 3214 ms, faster than 16.49% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 30.3 MB, less than 33.85% of Python3 online submissions for Partition Equal Subset Sum.
"""
# bottom up dp, O((target+1)*(sz+1))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sz = len(nums)
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2

        # dp[j][i] means j is reachable using first i elements
        dp = [[False] * (sz + 1) for _ in range(target + 1)]

        # sum 0 is reachable using no elements
        dp[0][0] = True

        for j in range(target + 1):
            for i in range(sz):
                if j - nums[i] >= 0:
                    # I am reachable
                    # if target - ith num reachable with i-1th nums, or
                    # if target reachable with i-1th nums
                    dp[j][i + 1] = dp[j - nums[i]][i] or dp[j][i]
                else:
                    dp[j][i + 1] = dp[j][i]

        return dp[target][-1]

    # example [1,2,5]:
    # - 1 is reachable using [1]
    # - 1 is reachable using [1 2]
    # - 1 is reachable using [1 2 5]
    # - 2 is reachable using [1] if 2-1 is reachable using []
    #                            or 2 reachable using []


"""
Runtime: 2165 ms (beats 49.1%)
Memory: 29.8 MB (beats 39.88%)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]


"""
TLE
"""
# recursion with memo -- O(2^(sz+1))
from collections import Counter


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        sz = len(nums)
        i = j = 0
        s = 0
        target = sum(nums) / 2
        if int(target) != target:
            return False

        def reachable(t, ns, memo):
            if (t, ns) in memo:
                return memo[(t, ns)]

            if t == 0:
                memo[(t, ns)] = True
                return True
            if t < 0:
                memo[(t, ns)] = False
                return False

            for i in range(len(list(ns))):
                if reachable(t - ns[i], ns[:i] + ns[i + 1 :], memo):
                    memo[(t, ns)] = True
                    return True

            memo[(t, ns)] = False
            return False

        memo = {}
        return reachable(target, tuple(nums), memo)


"""
TLE
"""
# stack attack -- O(2^(sz+1)) consider all the possibilities
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sz = len(nums)
        target = sum(nums) / 2
        if target - int(target) != 0:
            return False

        # stacks?
        todo = [(nums, 0)]
        while todo:
            ns, s = todo.pop()
            for i in range(len(ns)):
                if s + ns[i] == target:
                    return True
                elif s + ns[i] < target:
                    todo.append((ns[:i] + ns[i + 1 :], s + ns[i]))

        return False
