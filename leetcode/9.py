"""
Runtime: 114 ms, faster than 5.12% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 99.04% of Python3 online submissions for Palindrome Number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_pop_backward = x

        digits = []
        while x_pop_backward:
            x_pop_backward, r = divmod(x_pop_backward, 10)
            digits.append(r)

        i, j = 0, len(digits) - 1
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1

        return True


"""
Runtime: 106 ms, faster than 6.10% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 92.66% of Python3 online submissions for Palindrome Number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(str(x)) == list(str(x))[::-1]
