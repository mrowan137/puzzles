"""
Runtime: 560 ms, faster than 23.39% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 19.4 MB, less than 5.27% of Python3 online submissions for Random Pick with Weight.
"""
# O(Log N), bisection
import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        norm = sum(w)
        self.w = [wt / norm for wt in w]
        self.cumsum = reduce(
            lambda x, y: x + [(x[-1] if x else 0) + y], self.w, []
        )

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.cumsum, random.random())


"""
Runtime: 447 ms (beats 43.82%)
Memory: 19.2 MB (beats 8.3%)
"""
# Similar to above
class Solution:
    def __init__(self, w: List[int]):
        norm = sum(w)
        self.w = [wt / norm for wt in w]
        self.cumsum = reduce(
            lambda x, y: x + [(x[-1] if x else 0) + y], self.w, []
        )

    def pickIndex(self) -> int:
        rnd = random.random()
        # return bisect.bisect_left(self.cumsum, random.random())
        # bisection
        l, r = 0, len(self.cumsum) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if rnd < self.cumsum[m]:
                r = m - 1
            elif rnd > self.cumsum[m]:
                l = m + 1
            else:
                l = m
        return l


"""
Runtime: 2188 ms, faster than 19.63% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 18.7 MB, less than 68.53% of Python3 online submissions for Random Pick with Weight.
"""
# O(Log N), bisection
import random


class Solution:
    def __init__(self, w: List[int]):
        probs = [wt / sum(w) for wt in w]
        self.probs_cumsum = [sum(probs[: i + 1]) for i in range(len(probs))]

    def pickIndex(self) -> int:
        rand = random.random()

        # search for the first index i s.t. rand < w[i]
        l, r = 0, len(self.probs_cumsum) - 1
        while l <= r:
            mid = (l + r) // 2
            if rand < self.probs_cumsum[mid]:
                r = mid - 1  # search left
            elif rand > self.probs_cumsum[mid]:
                l = mid + 1  # search right
            elif rand == self.probs_cumsum[mid]:
                return mid  # found

        return l


"""
Runtime: 9836 ms, faster than 5.03% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 19.3 MB, less than 6.77% of Python3 online submissions for Random Pick with Weight.
"""
# O(N) for the draw, is not fast enough
import random


class Solution:
    def __init__(self, w: List[int]):
        # 0.25, 0.75
        # |---|---------|
        # 0  0.25      1.0
        # We can partition the unit segment
        # according to weights and sample uniformly
        # from [0, 1]; we select the index where that
        # number falls
        probs = [wt / sum(w) for wt in w]
        self.probs_cumsum = [sum(probs[: i + 1]) for i in range(len(probs))]

    def pickIndex(self) -> int:
        rand = random.random()
        i = 0
        while rand > self.probs_cumsum[i]:
            i += 1

        return i
