"""
Runtime: 314 ms, faster than 33.61% of Python3 online submissions for Longest String Chain.
Memory Usage: 15.7 MB, less than 33.43% of Python3 online submissions for Longest String Chain.
"""
from collections import defaultdict

# recursion with memo, O(N*k)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        m = defaultdict(list)
        for w in words:
            m[len(w)].append(w)

        memo = {}

        def longestChain(word):
            if word in memo.keys():
                return memo[word]
            N = len(word)
            transitions = [word[:i] + word[i + 1 :] for i in range(N)]
            res = 1
            for t in transitions:
                if t in m[N - 1]:
                    res = max(res, 1 + longestChain(t))

            memo[word] = res
            return res

        return max(longestChain(w) for w in words)


"""
Runtime: 229 ms, faster than 40.50% of Python3 online submissions for Longest String Chain.
Memory Usage: 14.7 MB, less than 63.40% of Python3 online submissions for Longest String Chain.
"""
# More DFS recursion with the memo
class Solution:
    def longestStrChain(self, words):
        # we want to form that longest chain
        # for each word, consider all predecessor
        # if it's there, we're the longest we seen

        def _(w, words, memo):
            if w in memo:
                return memo[w]

            res = 1
            preds = set([w[:i] + w[i + 1 :] for i in range(len(w))])
            for p in preds:
                if p in words:
                    res = max(res, 1 + _(p, words, memo))

            memo[w] = res
            return res

        res, memo = 0, {}
        words = set(words)
        for w in words:
            res = max(res, _(w, words, memo))

        return res


"""
Runtime: 640 ms, faster than 20.66% of Python3 online submissions for Longest String Chain.
Memory Usage: 14.9 MB, less than 34.93% of Python3 online submissions for Longest String Chain.
"""
# DFS with memo
class Solution:
    def longestStrChain(self, words):
        # we want to form that longest chain
        # for each word, consider all predecessor
        # if it's there, we're the longest we seen
        words = sorted(words, key=len)

        def _(wds, memo):
            if not wds:
                return 0
            wd = wds[-1]
            if wd in memo:
                return memo[wd]

            res = 0
            preds = set([wd[:i] + wd[i + 1 :] for i in range(len(wd))])
            for i in range(len(wds) - 1):
                if wds[i] in preds:
                    res = max(res, _(wds[: i + 1], memo))

            memo[wd] = 1 + res
            return 1 + res

        res, memo = 0, {}
        for i in range(len(words)):
            res = max(res, _(words[: i + 1], memo))

        return res


"""
Runtime: 148 ms, faster than 65.02% of Python3 online submissions for Longest String Chain.
Memory Usage: 14.8 MB, less than 44.00% of Python3 online submissions for Longest String Chain.
"""
# DFS with memoization, O(N*k) where k is the length of longest word
class Solution:
    def longest(self, words, memo, word):
        if word in memo.keys():
            return memo[word]

        res = 1  # longest substring for the current word; it is at least 1

        # for each predecessor, get the longest string chain
        predecessors = [word[:i] + word[i + 1 :] for i in range(len(word))]
        for p in predecessors:
            # longest substring could only be updated if predecessor is present
            if p in words:
                res = max(res, 1 + self.longest(words, memo, p))

        memo[word] = res

        return res

    def longestStrChain(self, words):
        # memo can store longest string chain for strings already seen
        # and words as a set can allow fast lookup if a predecessor is present
        memo, words = dict(), set([word for word in words])
        return max([self.longest(words, memo, word) for word in words])


"""
Runtime: 324 ms, faster than 25.03% of Python3 online submissions for Longest String Chain.
Memory Usage: 16.4 MB, less than 22.52% of Python3 online submissions for Longest String Chain.
"""
# memoization, O[N (log(N) + k) ], k is max length of a word
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # stores the longest string chain possible with a word;
        # if it's not seen before, longest string chain is 1
        longest = defaultdict(int)
        words = sorted(words, key=len)

        # for each word, get the predecessors
        # longest string chain will be 1 + longest
        # string chain possible from a predecessor
        for w in words:
            predecessors = [w[:i] + w[i + 1 :] for i in range(len(w))]
            longest[w] = 1 + max([longest[p] for p in predecessors])

        return max(longest.values())


"""
Runtime: 1716 ms, faster than 13.30% of Python3 online submissions for Longest String Chain.
Memory Usage: 14.9 MB, less than 44.00% of Python3 online submissions for Longest String Chain.
"""
# dp, but we should make this faster
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # O(N^2)
        # - dp[j] represents the longest string chain considering up to jth word
        # - for each word, if a predecessor is in the words[:j], say at ind i,
        #   then the longest string chain is 1 + dp[i]
        # - the words will need to be sorted so the longest string chain is built up
        #   sequentially
        N = len(words)
        dp = [1] * N
        words = sorted(words, key=len)

        for i in range(1, N):
            word = words[i]
            predecessors = [word[:i] + word[i + 1 :] for i in range(len(word))]

            for p in predecessors:
                v = float("-inf")
                if p in words[:i]:
                    j = 0
                    while words[j] != p:
                        j += 1
                    v = 1 + dp[j]

                dp[i] = max(dp[i], v)

        return max(dp)
