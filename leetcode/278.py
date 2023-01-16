"""
Runtime: 28 ms, faster than 81.31% of Python3 online submissions for First Bad Version.
Memory Usage: 14.3 MB, less than 43.29% of Python3 online submissions for First Bad Version.
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            elif not isBadVersion(m):
                l = m + 1

        return l
