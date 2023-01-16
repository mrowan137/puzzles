"""
Runtime: 28 ms, faster than 83.10% of Python3 online submissions for Divisor Game.
Memory Usage: 14 MB, less than 96.84% of Python3 online submissions for Divisor Game.
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        # two option:
        #   A. choose x, x < n and x | n
        #      e.g. n = 8, x = 1, 2, 4
        #   B. replace n --> n - x
        #      e.g. n = 8 --> 7, 6, 4
        #
        #
        #  SAMPLE GAMES
        #
        #  Alice winning nums: 2, 4,
        #  Bob winning nums:   1, 3,
        #
        #  n = 2
        #  Alice   | Bob
        #  ------------
        #  x1 n1   | A wins!
        #
        #  n = 3
        #  Alice   | Bob
        #  ------------
        #  x1 n2   | x1 n1
        #  B wins! |
        #
        #  n = 4
        #  Alice   | Bob
        #  ------------
        #  x1 n3   | x1 n2
        #  x1 n1   | A wins!
        #
        #  n = 5
        #  Alice   | Bob
        #  ------------
        #  x1 n4   | x2 n2
        #  x1 n1   | A wins!
        #
        # dp is an array of size n to track
        # if Alice is the winner from state n=(i+1);
        # 0 --> Alice, 1 --> Bob
        # dp = [1]*n  # assume Bob wins, our alg
        # will fill in the missing spaces
        # dp[0] = 1   # n = 1, Bob wins
        # dp[1] = 0   # n = 2, Alice wins
        # dp[2] = 1   # n = 3, Bob wins
        # dp[3] = 0   # n = 4, Alice wins
        # dp[4] = 1   # n = 5, Bob wins
        # ...
        # Logic: n=2 is winning for Alice.
        #        n=3 is winning for Bob.
        #        n=4 can reduce to n=2 so
        #            is winning for Alice
        #        n=5 reduce to n=4 so
        #            is winning for Bob
        #        n=6 reduce to n=4 so
        #            is winning for Alice
        # Summary: number is either even or odd
        # so divisible by one or two. Induction
        # hypothesis (sketch): Alice wins for n even, Bob
        # wins for n odd.  Base cases: n=1, n=2
        # (shown above).  Now assume n=k is even.
        # Then n%2 = 0 and n --> n - 2 which is even,
        # and by inductive hypothesis is a winning number
        # for Alice.  On the other hands, assume n=k is odd.
        # Since only an odd can divide an odd, (otherwise
        # the number is divisible by 2), and because the
        # difference of an odd and an odd is even, Bob
        # in this case will be given an even number, which
        # is a 'winning' state for Alice, and essentially
        # 'becomes' Alice, thus is in a winning state (i.e.
        # Alice loses)
        return ~n % 2
