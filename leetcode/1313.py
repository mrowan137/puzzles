"""
Runtime: 64 ms, faster than 84.90% of Python3 online submissions for Decompress Run-Length Encoded List.
Memory Usage: 14.9 MB, less than 26.59% of Python3 online submissions for Decompress Run-Length Encoded List.
"""


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        while nums:
            freq, val = nums.pop(0), nums.pop(0)
            res += freq * [val]

        return res
