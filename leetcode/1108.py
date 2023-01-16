"""
Runtime: 32 ms, faster than 46.86% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 14.2 MB, less than 32.74% of Python3 online submissions for Defanging an IP Address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        address = list(address)
        while address and address[0]:
            c = address.pop(0)
            res += c if c != "." else "[.]"

        return res
