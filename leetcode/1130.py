"""
Runtime: 32 ms, faster than 81.91% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 14.2 MB, less than 81.47% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
"""
# big brain O(N), stack attack
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # stack will be record of decreasing
        # so when we find one bigger, we know the last
        # is last < left && last < right, so greedily add
        # what give that min cost, and mid is discarded
        stack = [float("inf")]
        res = 0
        for a in arr:
            while a > stack[-1]:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)

        while len(stack) > 2:
            last = stack.pop()
            res += last * stack[-1]

        return res


"""
Runtime: 59 ms, faster than 37.42% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 14.3 MB, less than 61.37% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
"""
# O(N^2)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # compare neighbors x, y.  max(x, y) feeds up the
        # tree and can combine with another element
        # to contribute to the final cost.  discard the
        # min(x, y).  so the question rephrased to be:
        # min cost to reduce the array to just 1 elem?
        # x, y will contribute the cost x*y.  say x is
        # the min(x,y), y can be neighbors of x and
        # minimize the cost by take the smaller of that.
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1 : i] + arr[i + 1 : i + 2]) * arr.pop(i)

        return res


"""
Runtime: 300 ms, faster than 11.70% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 14.2 MB, less than 61.37% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
"""
# dp O(N^3) time, O(N^2) space
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        sz = len(arr)
        dp = [[float("inf")] * sz for _ in range(sz)]
        for i in range(sz):
            dp[i][i] = 0
        for j in range(1, sz):
            for i in range(j, -1, -1):
                for k in range(i, j):
                    dp[j][i] = min(
                        dp[j][i],
                        dp[k][i]
                        + dp[j][k + 1]
                        + max(arr[i : k + 1]) * max(arr[k + 1 : j + 1]),
                    )

        return dp[-1][0]


"""
Runtime: 573 ms, faster than 5.07% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 14.3 MB, less than 34.00% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
"""
# recursion with memo
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # sz-1 choices to partition to left and right
        def cost(a, memo):
            if tuple(a) in memo:
                return memo[tuple(a)]
            if len(a) <= 1:
                return 0
            sz = len(a)
            res = float("inf")
            for i in range(1, sz):
                l, r = a[:i], a[i:]
                res = min(
                    res,
                    cost(l, memo)  # left tree cost
                    + cost(r, memo)  # right tree cost
                    + max(l) * max(r),  # me cost
                )
            memo[tuple(a)] = res
            return res

        memo = {}
        return cost(arr, memo)


"""
TLE
"""
# recursion
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # sz-1 choices to partition to left and right
        def cost(a):
            if len(a) <= 1:
                return 0
            sz = len(a)
            res = float("inf")
            for i in range(1, sz):
                l, r = a[:i], a[i:]
                res = min(
                    res,
                    cost(l)  # left tree cost
                    + cost(r)  # right tree cost
                    + max(l) * max(r),  # me cost
                )
            return res

        return cost(arr)
