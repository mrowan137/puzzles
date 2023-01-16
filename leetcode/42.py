"""
Runtime: 88 ms, faster than 26.73% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 15.8 MB, less than 17.61% of Python3 online submissions for Trapping Rain Water.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        # cumulative heights up to current location, from left and right
        l, r = [0] * N, [0] * N

        # fill l and r
        h_max_l = -float("inf")
        h_max_r = -float("inf")
        for i in range(N):
            h_max_l = max(h_max_l, height[i])
            l[i] = h_max_l

            h_max_r = max(h_max_r, height[N - i - 1])
            r[N - i - 1] = h_max_r

        # compute final result
        return sum(min(l[i], r[i]) - height[i] for i in range(N))


"""
Runtime: 150 ms (beats 60.78%)
Memory: 16.3 MB (beats 7.45%)
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = [], []
        h_max = -float("inf")
        for h in height:
            h_max = max(h, h_max)
            l.append(h_max)

        h_max = -float("inf")
        for h in height[::-1]:
            h_max = max(h, h_max)
            r.append(h_max)

        r = r[::-1]

        res = []
        for i in range(len(height)):
            res.append(min(r[i], l[i]) - height[i])

        return sum(res)
