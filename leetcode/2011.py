"""
Runtime: 52 ms, faster than 74.86% of Python3 online submissions for Final Value of Variable After Performing Operations.
Memory Usage: 14.2 MB, less than 76.08% of Python3 online submissions for Final Value of Variable After Performing Operations.
"""


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        def op_to_num(s):
            if "-" in s:
                return -1
            elif "+" in s:
                return 1
            else:
                return 0

        return sum(map(op_to_num, operations))
