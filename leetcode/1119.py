"""
Runtime: 30 ms (beats 87.60%)
Memory: 13.8 MB (beats 51.74%)
"""


class Solution:
    def removeVowels(self, s: str) -> str:
        for vowel in ("a", "e", "i", "o", "u"):
            s = s.replace(vowel, "")
        return s
