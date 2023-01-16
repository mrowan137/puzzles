"""
Runtime: 48 ms, faster than 94.56% of Python3 online submissions for Shuffle String.
Memory Usage: 14.4 MB, less than 21.72% of Python3 online submissions for Shuffle String.
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sz = len(indices)
        d = {indices[i]: i for i in range(sz)}
        return "".join([s[d[i]] for i in range(sz)])
