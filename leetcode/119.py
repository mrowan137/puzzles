"""
Runtime: 32 ms, faster than 61.68% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 14.2 MB, less than 51.66% of Python3 online submissions for Pascal's Triangle II.
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0, 1, 0]
        for i in range(rowIndex):
            tmp = []
            for j in range(1, len(row)):
                tmp += [row[j] + row[j - 1]]

            row = [0] + tmp + [0]

        return row[1:-1]
