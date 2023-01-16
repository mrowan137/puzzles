"""
Runtime: 34 ms, faster than 76.84% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
Memory Usage: 13.7 MB, less than 97.37% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
"""
# O(N^2)
# we can make a smart observations; we need only to check the combinations
# of 2 digit numbers, since adding 3rd digit to 2 digit adds at a minimum,
# 100, to the two digit number @@.  an 100 is larger than any 2 digit num
# so 100 + @@  will be larger than @@ + &&.  thus we check the combos of 2.
class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [c for c in str(num)]
        res = float("inf")
        for i in range(4):
            for j in range(i + 1, 4):
                kl = [k for k in range(4) if k != i and k != j]
                k, l = kl[0], kl[1]
                res = min(
                    res,
                    int(nums[i] + nums[j]) + int(nums[k] + nums[l]),
                    int(nums[i] + nums[j]) + int(nums[l] + nums[k]),
                    int(nums[j] + nums[i]) + int(nums[k] + nums[l]),
                    int(nums[j] + nums[i]) + int(nums[l] + nums[k]),
                )
        return res
