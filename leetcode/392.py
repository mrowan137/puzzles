"""
Runtime: 112 ms, faster than 5.24% of Python3 online submissions for Is Subsequence.
Memory Usage: 15.8 MB, less than 5.89% of Python3 online submissions for Is Subsequence.
"""
# dp -- slower than two pointer but nice solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # edge cases: empty source string is subsequence of target
        #             empty target string has no subsequences
        if s == "":
            return True
        if t == "":
            return False

        # dp[j][i] is the number of matches considering
        # strings end at j and at i; if s[i] t[j] is a match,
        # then 'delete' the match char and dp[j][i] = 1 + dp[j-1][i-1].
        # if s[i] t[j] does not match, take the max of dp[j-1][i], dp[j][i-1]
        # to account for various cases:
        #    i is matching j is not   a b c, a b c q --> num match(abc, abc)
        #    i is not matching j is   a c q, a b c   --> num match(ac, abc)
        #    neither i or j match     a b q, a b r   --> num match(abq, ab)
        #                                            --> num match(ab, abr)
        #                                                (doesn't matter^)
        # so either both characters match, one matches in other, or neither is match
        # or in other words: delete a char that doesn't matter and continue compares
        M, N = len(s), len(t)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for j in range(1, N + 1):
            for i in range(1, M + 1):
                if s[i - 1] == t[j - 1]:
                    dp[j][i] = 1 + dp[j - 1][i - 1]
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j - 1][i])

        return dp[-1][-1] == min(len(s), len(t))


"""
Runtime: 32 ms, faster than 68.81% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.2 MB, less than 76.31% of Python3 online submissions for Is Subsequence.
"""
# pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            False
        if not s:
            return True

        # two pointer -- O( max(len(t), len(s)) )
        i = 0
        for j in range(len(t)):
            if i == len(s):
                break
            if s[i] == t[j]:
                i += 1

        return i == len(s)
