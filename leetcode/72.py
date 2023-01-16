"""
Runtime: 180 ms, faster than 57.27% of Python3 online submissions for Edit Distance.
Memory Usage: 17.7 MB, less than 73.03% of Python3 online submissions for Edit Distance.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)

        M, N = len(word1), len(word2)

        # let dp[j][i] is the min number of operations
        # to convert s[:i+1] to s[:j+1]
        dp = [[float("inf")] * (M + 1) for _ in range(N + 1)]

        # initial conditions -- 1 if different letter, 0 if same letter
        dp[1][1] = 0 if word1[0] == word2[0] else 1
        for i in range(M + 1):
            dp[0][i] = i  # i steps to turns "" into s[:i+1]
        for j in range(N + 1):
            dp[j][0] = j  # j steps to turns "" into s[:j+1]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                # compare
                # s[i],   s[j]
                # s[i-1], s[j]
                # s[i], s[j-1]
                if word1[i - 1] == word2[j - 1]:
                    # if match, discard the letter
                    # and compare substrings i-1, j-1:
                    #   (word1) xxA --> xx[A]
                    #   (word2) yyA --> yy[A]
                    #   ==> edits required: match(xx, yy)
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    # if the letters differ, discard one or both of the letters:
                    #   discard both
                    #   ------------
                    #     (word1) xxA --> xx[A]
                    #     (word2) yyB --> yy[B]
                    #     ==> edits required: 1 + match(xx, yy)
                    #
                    #   discard one
                    #   -----------
                    #     (i)
                    #       (word1) xxA --> xx[A]
                    #       (word2) yyB --> yyB
                    #     (ii)
                    #       (word1) xxA --> xxA
                    #       (word2) yyB --> yy[B]
                    #     ==> edits required: 1 + min( match(xx , yy ),
                    #                                  match(xxA, yy ),
                    #                                  match(xx , yyB) )
                    dp[j][i] = 1 + min(
                        dp[j - 1][i], dp[j][i - 1], dp[j - 1][i - 1]
                    )

        return dp[-1][-1]
