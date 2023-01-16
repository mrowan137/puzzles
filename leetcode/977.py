"""
Runtime: 256 ms, faster than 44.28% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 56.42% of Python3 online submissions for Squares of a Sorted Array.
"""
# Cleaner, iterate pointers from the ens
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)

        res = []
        l, r = 0, N - 1

        while l <= r:
            sql, sqr = nums[l] ** 2, nums[r] ** 2
            if sql > sqr:
                res.append(sql)
                l += 1
            else:
                res.append(sqr)
                r -= 1

        return res[::-1]


"""
Runtime: 477 ms, faster than 7.89% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.9 MB, less than 90.70% of Python3 online submissions for Squares of a Sorted Array.
"""
# Similar to above but starting from the inside
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)

        # find the min index
        i_min = 0
        minim = nums[0] ** 2
        for i in range(N):
            if minim > nums[i] ** 2:
                minim = nums[i] ** 2
                i_min = i

        l, r = i_min, i_min + 1
        res = []

        while l >= 0 and r <= N - 1:
            if nums[l] ** 2 <= nums[r] ** 2:
                res.append(nums[l] ** 2)
                l -= 1
            elif nums[l] ** 2 > nums[r] ** 2:
                res.append(nums[r] ** 2)
                r += 1

        # add the remaining
        if l >= 0:
            while l >= 0:
                res.append(nums[l] ** 2)
                l -= 1
        if r <= N - 1:
            while r <= N - 1:
                res.append(nums[r] ** 2)
                r += 1

        return res


"""
Runtime: 284 ms, faster than 34.21% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.5 MB, less than 5.23% of Python3 online submissions for Squares of a Sorted Array.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)

        # all negative
        if nums[0] < 0 and nums[-1] < 0:
            for i in range(N):
                nums[i] = nums[i] ** 2
            i, j = 0, N - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums
        # all positive
        elif nums[0] > 0:
            for i in range(N):
                nums[i] = nums[i] ** 2
            return nums

        # Else, we go from negative to positive

        # Find the element with smallest abs value
        i_min, n_min = 0, nums[0]
        for i, n in enumerate(nums):
            if abs(n) < abs(n_min):
                i_min, n_min = i, n

        l, r = i_min - 1, i_min + 1

        res = [n_min ** 2]

        while l >= 0 and r <= len(nums) - 1:
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[l] ** 2)
                l -= 1
            elif abs(nums[l]) > abs(nums[r]):
                res.append(nums[r] ** 2)
                r += 1

        # add the remainder
        if l >= 0:
            res += [nums[l - i] ** 2 for i in range(l + 1)]
        if r <= len(nums):
            res += [nums[i] ** 2 for i in range(r, len(nums))]

        return res
