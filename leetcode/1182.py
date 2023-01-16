"""
Runtime: 3437 ms, faster than 5.07% of Python3 online submissions for Shortest Distance to Target Color.
Memory Usage: 37.2 MB, less than 80.41% of Python3 online submissions for Shortest Distance to Target Color.
"""
# O(q Log(N) + N) using binary search;
# N to build the map, q Log(N) for binary search
from bisect import bisect_left


class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        sz = len(colors)

        # map from color to their indices in the list
        m = {1: [], 2: [], 3: []}
        for i in range(sz):
            m[colors[i]].append(i)

        def helper(q):
            i, c = q

            if not m[c]:
                # the color is not in the list!
                return -1

            # where would i be inserted to the list?
            j = bisect_left(m[c], i)

            if j == 0:
                # if we need to insert at the front
                return m[c][0] - i
            if j == len(m[c]):
                return i - m[c][-1]

            return min(m[c][j] - i, i - m[c][j - 1])

        return [helper(q) for q in queries]


"""
Runtime: 3578 ms, faster than 5.07% of Python3 online submissions for Shortest Distance to Target Color.
Memory Usage: 38.4 MB, less than 13.63% of Python3 online submissions for Shortest Distance to Target Color.
"""
# O(N), we precompute min distance to each color beforehand
# then the lookup is O(1)
class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        sz = len(colors)
        r1, r2, r3 = [-1] * sz, [-1] * sz, [-1] * sz  # distance on the right
        l1, l2, l3 = [-1] * sz, [-1] * sz, [-1] * sz  # distance on the left

        for i in range(sz):
            if colors[i] == 1:
                r1[i] = 0
            elif r1[i - 1] != -1:
                r1[i] = 1 + r1[i - 1]
            if colors[i] == 2:
                r2[i] = 0
            elif r2[i - 1] != -1:
                r2[i] = 1 + r2[i - 1]
            if colors[i] == 3:
                r3[i] = 0
            elif r3[i - 1] != -1:
                r3[i] = 1 + r3[i - 1]

        l1[-1] = 0 if colors[-1] == 1 else -1
        l2[-1] = 0 if colors[-1] == 2 else -1
        l3[-1] = 0 if colors[-1] == 3 else -1
        for i in range(sz - 2, -1, -1):
            if colors[i] == 1:
                l1[i] = 0
            elif l1[i + 1] != -1:
                l1[i] = 1 + l1[i + 1]
            if colors[i] == 2:
                l2[i] = 0
            elif l2[i + 1] != -1:
                l2[i] = 1 + l2[i + 1]
            if colors[i] == 3:
                l3[i] = 0
            elif l3[i + 1] != -1:
                l3[i] = 1 + l3[i + 1]

        def helper(q):
            i, c = q
            if c == 1:
                if r1[i] == -1 and l1[i] == -1:
                    return -1

                if r1[i] == -1:
                    res = l1[i]
                elif l1[i] == -1:
                    res = r1[i]
                else:
                    res = min(l1[i], r1[i])
            elif c == 2:
                if r2[i] == -1 and l2[i] == -1:
                    return -1

                if r2[i] == -1:
                    res = l2[i]
                elif l2[i] == -1:
                    res = r2[i]
                else:
                    res = min(l2[i], r2[i])
            elif c == 3:
                if r3[i] == -1 and l3[i] == -1:
                    return -1
                if r3[i] == -1:
                    res = l3[i]
                elif l3[i] == -1:
                    res = r3[i]
                else:
                    res = min(l3[i], r3[i])
            return res

        return [helper(q) for q in queries]


"""
TLE
"""
# O(N*M) where N is length of color and M is number of queries
class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        def helper(q):
            """Return the min distance from index to color"""
            i, c = q

            l = r = 0
            while i + l > 0 or i + r < len(colors) - 1:
                if colors[i + l] == c or colors[i + r] == c:
                    break
                l = max(-i, l - 1)
                r = min(len(colors) - i - 1, r + 1)

            if colors[i + l] == c:
                return -l
            if colors[i + r] == c:
                return r
            return -1

        return [helper(q) for q in queries]
