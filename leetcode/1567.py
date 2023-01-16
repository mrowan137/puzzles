"""
Runtime: 644 ms, faster than 67.87% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
Memory Usage: 28.2 MB, less than 49.28% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
"""
# Thinking through the problem:
# - dp(i, j) recursive approach? does not really work because product
#   depends on the numbers next to it; if n[i]*n[j] > 0, but n[i+1] or
#   n[j-1] is 0, you need to restart the count and would lose memory
#   of current largest; dp(i, j) not build directly from dp(i-k, j-k)
# - dpp, dpn approach: dpp[i] dpn[i] is the largest/least pos/neg sum
#   that ends in index i.  This allows to build dpp[i+1], dpn[i+1],
#   which can separate to cases:
#   n[i] = 0: dpp[i] = 0, dpn[i] = 0
#   n[i] > 0: dpp[i] = dpp[i-1] + 1, dpn[i] = dpn[i-1] + (dpn[i-1] != 0 )
#   n[i] < 0: dpp[i] = dpn[i-1] + (dpn[i-1] != 0), dpn[i] = dpp[i-1] + 1
#   with slight modification coming from edge cases.
#   n > 0: longest pos is prev longest pos + 1
#          longest neg is prev longest neg + 1, as long as there's a sequence to multiply
#   n < 0: longest neg is prev longest pos + 1
#          longest pos is prev longest neg + 1, as long as there's a sequence to multiply
# Why not (nums[i-1] != 0) instea of (dpn[i-1] != 0)?
# Well, that will fail for something like [1,2,3,4].  dpn would give [0,1,2,3]
# because we assumed implicitly there's a negative sequence to multiply when there is none.
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        dpp, dpn = [0] * N, [0] * N
        dpp[0] = int(nums[0] > 0)
        dpn[0] = int(nums[0] < 0)

        for i in range(1, N):
            if nums[i] > 0:
                # {1,-1} 1
                dpp[i] = dpp[i - 1] + 1
                dpn[i] = dpn[i - 1] + (dpn[i - 1] != 0)
            elif nums[i] < 0:
                # {1,-1} -1
                dpp[i] = dpn[i - 1] + (dpn[i - 1] != 0)
                dpn[i] = dpp[i - 1] + 1
            elif nums[i] == 0:
                dpp[i] = 0
                dpn[i] = 0

        return max(dpp)
