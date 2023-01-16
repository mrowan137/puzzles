"""
Runtime: 610 ms, faster than 45.08% of Python3 online submissions for Partition Array for Maximum Sum.
Memory Usage: 14.3 MB, less than 86.57% of Python3 online submissions for Partition Array for Maximum Sum.
"""


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # dp[i] represents the maximum sum considering
        # all arr[0] -- a[i-1].  Compute dp[i] by considering
        # e.g. arr = [1, 2, 2, 3, 4], k = 2; x is known
        # [x | x | x | x | x | ?] = dp
        # Loop through places you can put the partition
        # (here, before the 3 or the 4):
        # [1   2   2   3 | 4 ]  dp[5] = max(dp[5], dp[3] + 4)
        #
        # [1   2   2 | 3   4 ]  dp[5] = max(dp[5], dp[2] + 2*4)
        #
        # Some general dp advices:
        # It's a little like induction.
        # Assume dp[i] represents the desired solution.
        # How can you, given dp[0:i-1], to compute dp[i]?
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            curr_max = 0
            for j in range(1, min(k, i) + 1):
                curr_max = max(curr_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + j * curr_max)

        return dp[N]


# Partition array into contig subarrays of length (at most) k
# return max sum after partitioning
# Example:
# [1,2,3,4,5], k = 2
# [1 2], [3,4], [6] --> [2 2 4 4 6] --> 18
# [1, 3, 3, 6, 6] --> 19
# Idea:
# Keep track the largest array elements
# Iterate through, and shift window to maximize local sum
# Continue until full array is partitioned
# The greedy solution doesn't work!  Need to try again

from collections import defaultdict


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Track which elements are free to include in the window
        available = [1] * len(arr)

        # Function will maximize sum and update 'used'
        def maximize_window_sum(i):
            # i is a position in arr that will be contained by window
            # For a given position, loop over VALID windows
            # (in range, and contain only available spots);
            # loop over the windows and choose the best one
            if not available[i]:
                return 0
            print("i={}".format(i))
            window_starts_ = [
                j for j in range(max(i - k + 1, 0), min(i + 1, len(arr)))
            ]

            # Removed the starts that were already used
            window_starts = []
            for w in window_starts_:
                if available[w]:
                    window_starts.append(w)
                else:
                    pass

            next_used = i
            while next_used < len(arr) and available[next_used]:
                next_used += 1

            window_ends = [
                min(w + k, next_used, len(arr)) for w in window_starts
            ]

            # There may be now valid window spots for the passed ind,
            # we should exit
            print(
                "arr[i]={}, window_starts={}".format(
                    arr[i], [arr[w] for w in window_starts]
                )
            )
            if not window_starts:
                return 0

            windows = [w for w in zip(window_starts, window_ends)]

            sums = [sum(arr[w[0] : w[1]]) for w in windows]
            lens = [w[1] - w[0] for w in windows]
            mx = [max(arr[w[0] : w[1]]) for w in windows]
            ind_min = max(
                window_starts,
                key=lambda j: mx[j - window_starts[0]]
                * lens[j - window_starts[0]]
                - sums[j - window_starts[0]],
            )
            # Update which elements now used
            used = [j for j in range(ind_min, min(ind_min + k, len(arr)))]

            for j in used:
                available[j] = 0

            add = (
                max(arr[w] for w in window_starts)
                * lens[ind_min - window_starts[0]]
            )

            print("availe: ", available)
            print("res += {}".format(add))

            print("-------")
            return add

        # For the final tally
        res = 0

        # Get inds of the largest
        val_to_ind = defaultdict(list)
        for i in range(len(arr)):
            val_to_ind[arr[i]].append(i)

        # Iterate through largest elements and greddily maximize sum
        for v in sorted(arr)[::-1]:  # sorted(val_to_ind)[::-1]:
            curr_inds = val_to_ind[v]
            while curr_inds:
                res += maximize_window_sum(curr_inds.pop())

        return res
