"""
Runtime: 85 ms (beats 90.12%)
Memory: 16.2 MB (beats 49.70%)

consider the subset problem from [nmin, n], of [nmin, nmax].
let dp[i] == the max score possible on [nmin, n].
it gives the recursive formula:
    dp[i] = max(n * cnt[n] + dp[i - 2], if CHOOSE to delete entry i
                dp[i - 1]             , if CANNOT delete entry i
            )                           [which includes it was deleted already,
                                         and I choose not to delete]
IF I am deleted, I sum with dp[i - 2] and my contribution n * cnt[n];
IF I am not deleted, my score is simply dp[i - 2].
what about the n>nums[i] that would be deleted in the first case?
kick the can down the road to when we arrive there, sorts itself out.
"""
from collections import Counter, defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nmin, nmax = min(nums), max(nums)

        dp = defaultdict(int)

        c = Counter(nums)
        for i in range(nmax - nmin + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + c[i + nmin] * (i + nmin))

        return max(dp.values())
