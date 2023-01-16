"""
Runtime: 324 ms, faster than 20.64% of Python3 online submissions for Ugly Number II.
Memory Usage: 14.4 MB, less than 23.31% of Python3 online submissions for Ugly Number II.
"""


class Ugly:
    def __init__(self):
        N = 1690

        # store the ugly numbers
        self.dp = [1]

        # search here for the next ugly number
        # each number here satisfies c*2 or c*3 or c*5 larger than
        # largest computed ugly number; if none is larger we'll
        # remove it from the list
        candidates = [1]

        # the ugly factors
        pfs = [2, 3, 5]

        # precompute: compute the smallest possibility from the candidates
        # add it to the list, add it also as a candidate; remove any candidate
        # ci that is smaller than the added number, since all ugly numbers
        # ci*2, ci*3, ci*5 are already in the list.
        while len(self.dp) < N:
            curr = self.dp[-1]

            m = float("inf")
            for c in candidates:
                for p in pfs:
                    if c * p > curr:
                        m = min(m, c * p)
            self.dp.append(m)
            candidates += [m]
            candidates = [
                c for c in candidates if any([c * p > m for p in pfs])
            ]


U = Ugly()


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return U.dp[n - 1]
