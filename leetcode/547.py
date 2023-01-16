"""
Runtime: 298 ms, faster than 25.86% of Python3 online submissions for Number of Provinces.
Memory Usage: 14.8 MB, less than 33.00% of Python3 online submissions for Number of Provinces.
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        sz = len(isConnected)
        seen = set()

        def find(me, friends):
            if not me in seen:
                seen.add(me)
                for i, f in enumerate(friends):
                    if f:
                        find(i, isConnected[i])
                return 1
            else:
                return 0

        res = 0
        for i in range(sz):
            res += find(i, isConnected[i])

        return res


"""
Runtime: 184 ms, faster than 85.45% of Python3 online submissions for Number of Provinces.
Memory Usage: 14.9 MB, less than 34.36% of Python3 online submissions for Number of Provinces.
"""
# DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        # approach: visit each city, record it is seen,
        #           and for each connected city, recurse
        #
        seen = set()  # record if a city is seen
        res = 0  # number of provinces

        # dfs
        def visit(i):
            # record that we visited the city
            seen.add(i)

            # for each potentially connected city
            for j, val in enumerate(isConnected[i]):
                if val and not j in seen:
                    visit(j)

        # invariant: seen contains all cities visited so far,
        #            res is the number of provinces so far
        for i in range(N):
            # if city is not seen, fill out the full province and increment the count
            if not i in seen:
                visit(i)
                res += 1

        return res


"""
Runtime: 355 ms, faster than 10.39% of Python3 online submissions for Number of Provinces.
Memory Usage: 14.7 MB, less than 51.41% of Python3 online submissions for Number of Provinces.
"""
# Iteration
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)

        seen = set()  # record if a city is seen
        res = 0  # number of provinces

        for i in range(N):
            if not i in seen:
                toVisit = [i]
                while toVisit:
                    curr = toVisit.pop()
                    seen.add(curr)
                    toVisit += [
                        j
                        for j, val in enumerate(isConnected[curr])
                        if val and not j in seen
                    ]
                    # for j,val in enumerate(isConnected[curr]):
                    #    if val and j not in seen:
                    #        toVisit.append(j)
                res += 1

        return res
