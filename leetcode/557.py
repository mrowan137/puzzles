"""
Runtime: 39 ms, faster than 61.94% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.9 MB, less than 61.93% of Python3 online submissions for Reverse Words in a String III.
"""
# one liner
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split(" ")])


"""
Runtime: 104 ms, faster than 12.18% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 15.2 MB, less than 11.34% of Python3 online submissions for Reverse Words in a String III.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseWord(s):
            # s is a str
            # ret: reversed string
            s = list(s)
            l, r = 0, len(s) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            return "".join(s)

        words = s.split(" ")

        return " ".join(reverseWord(w) for w in words)
