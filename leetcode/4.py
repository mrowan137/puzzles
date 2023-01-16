"""
See: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
Runtime: 80 ms, faster than 97.76% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.6 MB, less than 22.63% of Python3 online submissions for Median of Two Sorted Arrays.
"""


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # want to split nums1 and nums 2 into sets [A1/A2], [B1/B2]
        # so that
        #   1. len(A1 + B1) == len(A2 + B2)
        #   2. max(A1 + B2) == min(A2 + B2)
        # strategy: binary search

        # arrange shorter to be first
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        sz1, sz2 = len(nums1), len(nums2)

        # binary search: indices of nums1
        # and half_size to compute index in nums2
        lo, hi, hlf = 0, sz1, (sz1 + sz2 + 1) // 2

        while lo <= hi:
            i = (lo + hi) // 2
            j = int(hlf - i)
            # note nums2[j-1] < nums2[j] because sorted, so only
            # need to compare nums1[i], other part of R set
            if i < sz1 and nums2[j - 1] > nums1[i]:
                lo = i + 1
            elif i > 0 and nums2[j] < nums1[i - 1]:
                hi = i - 1
            else:
                # now nums2[j-1] <= nums1[i  ]
                # and nums2[j  ] >= nums1[i-1]
                # so the divide is as desired
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (sz1 + sz2) % 2 == 1:
                    return max_of_left

                if i == sz1:
                    min_of_right = nums2[j]
                elif j == sz2:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
