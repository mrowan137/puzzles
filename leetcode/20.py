"""
Runtime: 28 ms, faster than 84.17% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.1 MB, less than 87.54% of Python3 online submissions for Valid Parentheses.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # pop results off the stack
        cl_to_op = {")": "(", "]": "[", "}": "{"}
        s, res = list(s), ""
        for c in s:
            if c in cl_to_op.keys():
                if not res or res and not cl_to_op[c] == res[-1]:
                    return False
                res = res[:-1]
            elif c in cl_to_op.values():
                res += c

        return not res
