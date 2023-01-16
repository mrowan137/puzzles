"""
A cafeteria table consists of a row of N seats, numbered from 1 to N from left
to right. Social distancing guidelines require that every diner be seated such
that K seats to their left and K seats to their right (or all the remaining
seats to that side if there are fewer than K) remain empty. There are currently
M diners seated at the table, the ith of whom is in seat S_i.  No two diners are
sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the
table without social distancing guidelines being violated for any new or
existing diners, assuming that the existing diners cannot move and that the
additional diners will cooperate to maximize how many of them can sit down.
"""
from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S = [-K] + sorted(S) + [N + K + 1]

    res = 0
    for i in range(len(S) - 1):
        s1, s2 = S[i], S[i + 1]
        res += max((s2 - s1 - 1 - K) // (K + 1), 0)

    return res
