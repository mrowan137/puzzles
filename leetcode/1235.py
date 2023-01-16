"""
Runtime: 599 ms, faster than 82.63% of Python3 online submissions for Maximum Profit in Job Scheduling.
Memory Usage: 27.7 MB, less than 59.89% of Python3 online submissions for Maximum Profit in Job Scheduling.
"""


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # sort jobs according to end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda j: j[1])

        # dp is a list of [end, profit]
        # the max profit up to end
        # we need to record end because
        # we find the biggest profit possible with s
        dp = [[0, 0]]

        for s, e, p in jobs:
            # find the most recent (rightmost)
            # end e in dp such that e <= s
            # bisect_left (vector, x)
            # finds the first (leftmost) x in vector.
            # so we find the leftmost s+1, then move
            # one to the left
            i = bisect.bisect_left(dp, [s + 1]) - 1

            # take the profit if it improves the max profit
            if dp[i][1] + p >= dp[-1][1]:
                dp.append([e, dp[i][1] + p])

        # the max profit possible
        return dp[-1][1]
