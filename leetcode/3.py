"""
Runtime: 303 ms, faster than 18.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 6.39% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)

        # return index in [0, 25] from lower case num
        count = defaultdict(int)

        i, j = 0, 0
        res = 0

        while j < N:
            # update letter count
            count[s[j]] += 1
            j += 1

            # scoot up window if repeats
            while max(count.values()) > 1:
                count[s[i]] -= 1
                i += 1

            # update result
            res = max(res, j - i)

        return res


"""
Runtime: 192 ms, faster than 21.89% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        num_seen = defaultdict(int)
        longest = 0
        i, res = 0, 0
        for j, c in enumerate(s):
            num_seen[c] += 1
            while max(num_seen.values()) > 1 and i < j:
                num_seen[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)

        return res
