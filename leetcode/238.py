"""
Runtime: 241 ms (beats 79.60%)
Memory: 22.3 MB (beats 26.45%)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        l = [1] * sz  # cumulative products on the left, except i
        r = [1] * sz  # cumulative products on the right

        for i in range(1, sz):
            l[i] = l[i - 1] * nums[i - 1]
        for i in range(sz - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        res = [0] * sz

        for i in range(sz):
            res[i] = l[i] * r[i]

        return res


"""
Runtime: 242 ms (beats 78.18%)
Memory: 21.4 MB (beats 52.66%)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(1) memory
        sz = len(nums)
        res = [1] + [0] * (sz - 1)
        for i in range(1, sz):
            res[i] = nums[i - 1] * res[i - 1]

        r = 1
        for i in range(sz - 1, -1, -1):
            res[i] = r * res[i]
            r *= nums[i]

        return res


"""
Runtime: 297 ms (beats 47.15%)
Memory: 22.3 MB (beats 29.96%)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l[i], r[i] are left, right products up to i
        sz = len(nums)
        l, r, res = [0] * sz, [0] * sz, [0] * sz
        for i in range(sz):
            l[i] = nums[i] * (l[i - 1] if i >= 1 else 1)
            r[sz - 1 - i] = nums[sz - 1 - i] * (r[sz - i] if i >= 1 else 1)

        for i in range(sz):
            res[i] = (l[i - 1] if i >= 1 else 1) * (
                r[i + 1] if i < sz - 1 else 1
            )

        return res


"""
Runtime: 243 ms (beats 76.80%)
Memory: 21.2 MB (beats 74.26%)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from collections import Counter
        from functools import reduce

        product = lambda arr: reduce((lambda x, y: x * y), arr)
        c, sz = Counter(nums), len(nums)
        if c[0] == 0:
            p = product(nums)
            return [p // nums[i] for i in range(sz)]

        elif c[0] == 1:
            wh = nums.index(0)
            nums[wh] = 1
            res = [0] * sz
            res[wh] = product(nums)
            return res

        elif c[0] > 1:
            return [0] * sz
