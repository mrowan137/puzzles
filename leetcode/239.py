"""
Runtime: 2646 ms, faster than 44.11% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.2 MB, less than 48.04% of Python3 online submissions for Sliding Window Maximum.
"""
# dp O(N)
# insight here is we divide nums into regions of size window.
# the special case our window aligns with those region, we could take the max going to left.
# if we overlap across two regions, just take max of two possibilities going away from separator.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sz = len(nums)

        # max going to left, to right
        l, r = [float("-inf")] * sz, [float("-inf")] * sz

        for i in range(sz):
            if i % k == 0:
                r[i] = nums[i]
            else:
                r[i] = max(nums[i], r[i - 1])

            j = sz - 1 - i
            if j % k == 0:
                l[j] = nums[j]
            else:
                l[j] = max(nums[j], l[(j + 1) % sz])

        res = []
        for i in range(sz - k + 1):
            res.append(max(l[i], r[i + k - 1]))

        return res


"""
Runtime: 1821 ms, faster than 82.25% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.7 MB, less than 22.30% of Python3 online submissions for Sliding Window Maximum.
"""
# deque O(N)
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # q stores decreasing list of largest numbers (idx) in the current window
        q = deque()
        res = []
        for i in range(len(nums)):
            # we saw a new num. which would clearly be in the window.
            # squeeze out anything less than it, until you hit the wall.
            # q = [5 4 3 2 1 0] --> nums[i] = 4 --> q = [5 4 <-- 4] = [5 4 4]
            # who cares about those smaller number, they would not be max.
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            # keep q in the legal range.
            # i is current place. i == k + q[0] means q[0] out of range.
            if q[0] + k == i:
                q.popleft()

            # we could add our result here. start adding when we pass first window.
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


"""
TLE
"""
# brute force
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sz = len(nums)
        res = []
        window = deque(nums[:k])

        # sweep through nums
        for i in range(k, sz):
            res.append(max(window))
            window.popleft()
            window.append(nums[i])

        return res + [max(window)]


"""
Runtime: 1972 ms, faster than 47.70% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.1 MB, less than 62.99% of Python3 online submissions for Sliding Window Maximum.
"""
# dynamic programming
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        # l, r keeps the max moving from left, right
        # of a given k window.  these two lists give
        # all the information needed to track max k
        l, r = [-float("inf")] * N, [-float("inf")] * N

        # construct l and r
        for i in range(N):
            # fill l
            if i % k == 0:
                l[i] = nums[i]
            else:
                l[i] = max(nums[i], l[i - 1])

            # fill r
            j = N - i - 1
            if (j + 1) % k == 0:
                r[j] = nums[j]
            else:
                r[j] = max(nums[j], r[j + 1]) if j + 1 < N else nums[j]

        # construct answer
        # matrix: [1 2 1 2 3 2], k = 3
        #      l: [1 2 2|2 3 3]
        #      r: [2 2 1|3 3 2]
        #    res:   |   | |, i = 1
        #    max of left side (r[i]) and right side (l[i+k-1])
        res = []
        for i in range(N - k + 1):
            res.append(max(l[i + k - 1], r[i]))

        return res


"""
Runtime: 1940 ms, faster than 50.67% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 29.9 MB, less than 68.82% of Python3 online submissions for Sliding Window Maximum.
"""
# deque
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Algorithm: deque will store window max in first location,
        #            and only indices within the current window
        #     - if new element is larger than prevs, we don't care about the
        #       prev inds! this will be a max in the next sliding window
        #     - if new element is smaller than prevs, keep it! it may be
        #       a max in the next sliding window
        # 1. pop from back of deque elements smaller than that to be added
        # 2. add the new element to the deque
        # 3. remove q[0] if it's out of range
        # 4. add answer if we've seen the full first winow or beyond
        N = len(nums)

        # define: q[0] is the max within the current window
        q = deque()

        res = []
        for i in range(N):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
