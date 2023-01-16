"""
Runtime: 325 ms, faster than 5.03% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.1 MB, less than 36.08% of Python3 online submissions for Merge Intervals.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        for i in sorted(intervals):
            if res and res[-1][-1] >= i[0]:
                res[-1][-1] = max(res[-1][-1], i[1])
            else:
                res.append(i)
        return res


"""
Runtime: 209 ms, faster than 22.07% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.9 MB, less than 7.06% of Python3 online submissions for Merge Intervals.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals = sorted(intervals)
        # count the num of
        # |||||||
        #     ||||||||||
        #      ||||||||||
        #                  |||
        start, end = intervals[0]

        for i in intervals[1:]:
            b, e = i
            if b <= end:
                start = min(b, start)
                end = max(e, end)
            else:
                res.append([start, end])
                start, end = b, e

        res.append([start, end])

        return res


"""
Runtime: 80 ms, faster than 91.82% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.1 MB, less than 55.25% of Python3 online submissions for Merge Intervals.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # disjoint union of intervals
        res = []

        # invariant: res contains all union intervals seen so far
        # add to the current union if curr start lteq prev,
        # start a new union otherwise
        for i in sorted(intervals):
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(i[1], res[-1][-1])
            else:
                res.append(i)

        return res


"""
Runtime: 596 ms, faster than 5.02% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.1 MB, less than 55.25% of Python3 online submissions for Merge Intervals.
"""
# O(N Log N) for sorting, O(N) for loop
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Idea: sort according to begin times
        # Add one by one, as long as begining happens before an end
        intervals = sorted(intervals)
        res = []

        begins, ends = [], []
        for interval in intervals:
            b, e = interval
            if (not begins and not ends) or b <= max(ends):
                begins.append(b)
                ends.append(e)
            else:
                res.append([min(begins), max(ends)])
                begins = [b]
                ends = [e]

        if begins and ends:
            res.append([min(begins), max(ends)])

        return res


"""
Runtime: 80 ms, faster than 90.98% of Python3 online submissions for Merge Intervals.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # strategy: count number of starts>end
        intervals = sorted(intervals)
        s_min, e_max = intervals[0]

        res = []
        for i in intervals:
            s = i[0]
            if s > e_max:
                res.append([s_min, e_max])
                s_min = min(s, i[0])

            e_max = max(i[1], e_max)

        # add the final interval
        res.append([s_min, e_max])

        return res
