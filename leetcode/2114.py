"""
Runtime: 70 ms, faster than 27.33% of Python3 online submissions for Maximum Number of Words Found in Sentences.
Memory Usage: 14 MB, less than 41.47% of Python3 online submissions for Maximum Number of Words Found in Sentences.
"""


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = float("-inf")
        for s in sentences:
            res = max(res, len(s.split(" ")))
        return res
