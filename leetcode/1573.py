"""
Runtime: 333 ms, faster than 21.93% of Python3 online submissions for Number of Ways to Split a String.
Memory Usage: 15.8 MB, less than 13.98% of Python3 online submissions for Number of Ways to Split a String.
"""


class Solution:
    def numWays(self, s: str) -> int:
        nums, mx = [int(c) for c in s], 10 ** 9 + 7

        if not sum(nums) % 3 == 0:
            return 0

        target = sum(nums) // 3
        if target == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % mx

        a, b = 0, 0
        cnt = 0
        for n in nums:
            cnt += n
            if cnt == target and cnt:
                a += 1
            elif cnt == 2 * target and cnt:
                b += 1

        return a * b % mx
