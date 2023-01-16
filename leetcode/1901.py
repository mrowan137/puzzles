"""
Runtime: 1404 ms, faster than 54.76% of Python3 online submissions for Find a Peak Element II.
Memory Usage: 45.5 MB, less than 81.50% of Python3 online submissions for Find a Peak Element II.
"""


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # need O (n log m soln)
        #
        # sort the rows and look for 1 is greater than surrounders.
        #     - end of th rows meant I been greater than anything in those row
        #     - greater than above, belowed meant was greater than any the above, belowd
        #     - it's all the unique nums, thus there guarantees to have the max num last cols
        #     - we could just take that max num, all the last elems of sorted rows
        m = [float("-inf"), [0, 0]]
        for i, row in enumerate(mat):
            v, j = sorted(zip(row, range(len(row))), key=lambda kv: kv[0])[-1]
            m = max(m, [v, [i, j]])
