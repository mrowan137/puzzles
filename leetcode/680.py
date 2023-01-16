"""
Runtime: 160 ms, faster than 68.77% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.6 MB, less than 20.68% of Python3 online submissions for Valid Palindrome II.
"""


class Solution:
    def validPalindrome(self, s: str, deletions=0) -> bool:
        # we might need to delete
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if deletions == 0:
                    # check if either is a palindrome skipping
                    return self.validPalindrome(
                        s[l + 1 : r + 1], 1
                    ) or self.validPalindrome(s[l:r], 1)
                else:
                    return False

            l += 1
            r -= 1

        return True
