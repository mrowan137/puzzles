"""
Runtime: 56 ms, faster than 96.50% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.8 MB, less than 5.02% of Python3 online submissions for Two Sum II - Input array is sorted.
"""
# Cleaner rewrite
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        l, r = 0, N - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]


"""
Runtime: 64 ms, faster than 66.97% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.6 MB, less than 62.27% of Python3 online submissions for Two Sum II - Input array is sorted.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            # s is the `sum`
            s = numbers[i] + numbers[j]

            if s < target:
                # increase the sum
                i += 1
            elif s > target:
                # decrease the sum
                j -= 1

            elif s == target:
                return [i + 1, j + 1]
