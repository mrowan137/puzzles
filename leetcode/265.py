"""
Runtime: 104 ms, faster than 86.89% of Python3 online submissions for Paint House II.
Memory Usage: 14.5 MB, less than 18.25% of Python3 online submissions for Paint House II.
"""
# O(n*k) loop in i and j
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # j is the house idx, i the colors
        M, N = len(costs[0]), len(costs)

        dp = [[0] * M for _ in range(N)]

        for j in range(N):  # house
            # get idx of smallest and second smallest cumulative cost
            # considering up to j-1 houses
            i_min, v_min = None, float("inf")
            i_min_2, v_min_2 = None, float("inf")

            for i in range(M):  # cost
                # if curr less than min val seen so far
                if dp[j - 1][i] < v_min:
                    i_min_2, v_min_2 = i_min, v_min
                    i_min, v_min = i, dp[j - 1][i]
                # else, if curr less than 2nd min val seen so far (but >= min)
                elif dp[j - 1][i] < v_min_2:
                    i_min_2, v_min_2 = i, dp[j - 1][i]

            for i in range(M):  # colors
                if i == i_min:
                    dp[j][i] = costs[j][i] + v_min_2
                else:
                    dp[j][i] = costs[j][i] + v_min

        return min(dp[-1])


"""
Runtime: 120 ms, faster than 64.44% of Python3 online submissions for Paint House II.
Memory Usage: 14.2 MB, less than 85.82% of Python3 online submissions for Paint House II.
"""
# O(n*k^2) for loop in M, N, and min calc
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # j is the house idx, i the colors
        M, N = len(costs[0]), len(costs)

        dp = [[0] * M for _ in range(N)]

        for j in range(N):  # house
            dp_j_prev = [cumulative_cost for cumulative_cost in dp[j - 1][:]]
            for i in range(M):  # colors
                # get min cumulative cost of values except current i
                v_min = min(dp_j_prev[:i] + dp_j_prev[i + 1 :])
                dp[j][i] = costs[j][i] + v_min

        return min(dp[-1])
