"""
Runtime: 60 ms, faster than 6.17% of Python3 online submissions for Decode Ways.
Memory Usage: 14.4 MB, less than 40.66% of Python3 online submissions for Decode Ways.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        # helper function for decoding up to length 2
        def valid(s):
            return 1 if s in [str(x) for x in range(1, 27)] else 0

        # dp[i] is the number of ways to decode string s[:i+1]
        dp = [0] * (N + 2)

        # initial conditions: potentially 1 way to decode length one string at ind 0
        # but 0 ways to decode length two string at ind 0
        dp[0], dp[1] = 0, 1

        # number of ways to decode string ending in i is sum of
        # num ways to decode string ending in i-1 (given s[i]          is valid), and
        # num ways to decode string ending in i-2 (given s[i-1] + s[i] is valid)
        for i in range(2, N + 2):
            dp[i] = dp[i - 1] * valid(s[i - 2 : i - 1]) + dp[i - 2] * valid(
                s[i - 3 : i - 1]
            )

        return dp[-1]


"""
Runtime: 34 ms (beats 80.96%)
Memory: 13.8 MB (beats 77.3%)
"""

from collections import deque, defaultdict


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Dynamic programming
        """
        # dp[i] represents number of ways to decode string of length i
        # consider last digit _ and last two digits __
        # if _  is (1--9),   it contributes dp[i-1] new valid decodings
        # if __ is (10--26), it contributes dp[i-2] new valid decodings
        dp = [0] * (len(s) + 1)

        # initialization; one way to decode the empty string
        dp[0], dp[1] = 1, 1 if s[0] != "0" else 0

        for i in range(2, len(s) + 1):
            _, __ = int(s[i - 1 : i]), int(s[i - 2 : i])
            if 1 <= _ and _ <= 9:
                dp[i] += dp[i - 1]
            if 10 <= __ and __ <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


"""
TLE
"""
from collections import deque, defaultdict


class Solution:
    def numDecodings(self, s: str) -> int:
        # bfs: enumerate all possibilities
        valid = lambda x: (int(x) < 27) * (x[0] != "0")
        dic = defaultdict(lambda: "?")
        for i in range(26):
            dic[str(i + 1)] = chr(65 + i)

        stack, seen, res = deque([list(s)]), set(), 0
        while stack:
            curr = stack.pop()
            res += all(map(valid, curr))
            seen.add("".join(map(lambda x: dic[x], curr)))

            # generate all new possibilities if not already seen
            for i in range(len(curr) - 1):
                a, b = curr[i], curr[i + 1]
                if not valid(a + b):
                    continue
                new = curr[:i] + [a + b] + curr[i + 2 :]
                new_s = "".join(map(lambda x: dic[x], new))
                if not new_s in seen:
                    stack.append(new)

        return res
