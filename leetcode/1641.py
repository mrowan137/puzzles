"""
Runtime: 6628 ms, faster than 8.28% of Python3 online submissions for Count Sorted Vowel Strings.
Memory Usage: 89 MB, less than 5.06% of Python3 online submissions for Count Sorted Vowel Strings.
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:

        d = {
            "a": ["a", "e", "i", "o", "u"],
            "e": ["e", "i", "o", "u"],
            "i": ["i", "o", "u"],
            "o": ["o", "u"],
            "u": ["u"],
        }

        res = ["a", "e", "i", "o", "u"]
        for i in range(n - 1):
            tmp = []
            for v in res:
                tmp += [v + x for x in d[v[-1]]]
            res = tmp

        return len(res)
