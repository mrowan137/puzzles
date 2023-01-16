"""
Runtime: 36 ms, faster than 83.78% of Python3 online submissions for Word Break.
Memory Usage: 14.3 MB, less than 88.89% of Python3 online submissions for Word Break.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sz = len(s)

        dp = [True] + [False] * sz

        for i in range(1, sz + 1):
            for j in range(i + 1):
                dp[i] = dp[i] or (dp[j] and s[j:i] in wordDict)

        return dp[-1]


"""
Runtime: 40 ms, faster than 68.48% of Python3 online submissions for Word Break.
Memory Usage: 14.5 MB, less than 45.64% of Python3 online submissions for Word Break.
"""
# dp again!
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        # dp[i] represents current loc is reachable using the dict
        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(1, N + 1):
            for w in wordDict:
                if i - len(w) >= 0:
                    if dp[i - len(w)] == True and s[i - len(w) : i] == w:
                        dp[i] = True

        return dp[-1]


"""
Runtime: 32 ms, faster than 92.45% of Python3 online submissions for Word Break.
Memory Usage: 14.2 MB, less than 87.79% of Python3 online submissions for Word Break.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # strategy: dp
        # initial conditions
        dp = [True] + [False] * (len(s))  # dp represents that string up to i
        # is buildable from words in the dict

        # at each position of target string, consider each
        # word in the dict, and the backed-out position
        for j in range(len(s)):
            for w in wordDict:
                i = j + 1 - len(w)
                if s[i : j + 1] == w and dp[i]:
                    dp[j + 1] = True

        return dp[-1]


# TLE
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Recursioon: iterate through string until
        # find a word in the dict, then call wordBreak on the remaining
        # terminate if reach the end of string

        # exit condition
        if s in wordDict:
            return True

        for w in set(wordDict):
            sub = s[: len(w)]
            if sub == w:
                tmp = self.wordBreak(s[len(w) :], wordDict)
                if tmp:
                    return True

        return False
