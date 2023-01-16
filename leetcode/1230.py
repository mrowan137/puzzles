"""
Runtime: 1384 ms, faster than 38.29% of Python3 online submissions for Toss Strange Coins.
Memory Usage: 51.6 MB, less than 46.20% of Python3 online submissions for Toss Strange Coins.
"""


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        sz = len(prob)

        # dp[j][i] is the prob to get j head given i flips
        dp = [[0] * (sz + 1) for _ in range(target + 1)]

        # Initial conditions
        dp[0][0] = 1.0  # 0 heads in 0 flips happens with p = 1

        for j in range(target + 1):
            for i in range(1, sz + 1):
                # j heads in i flips can come from
                # j -1 heads in i-1 flips and a heads
                # or j heads in i-1 flips and a tails
                dp[j][i] = dp[j - 1][i - 1] * prob[i - 1] * (j >= 1) + dp[j][
                    i - 1
                ] * (1 - prob[i - 1])

        return dp[-1][-1]
