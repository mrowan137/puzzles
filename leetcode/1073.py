"""
Runtime: 60 ms, faster than 94.37% of Python3 online submissions for Adding Two Negabinary Numbers.
Memory Usage: 14 MB, less than 92.61% of Python3 online submissions for Adding Two Negabinary Numbers.
"""
# Clever O(M + N)
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        carry = 0  # defines as the current add, correct for current digit
        while arr1 or arr2 or carry:
            # get digits to add
            x = 0 if not arr1 else arr1.pop()
            y = 0 if not arr2 else arr2.pop()

            # addend is the 0th digits of x+y+carry
            res.append((carry + x + y) & 1)

            # carry for next round will be 1st digits of x+y+carry,
            # dropping the 0th digit we just used, and multiply
            # a minus sign to account for the flopping sign
            carry += x + y
            carry = -(carry >> 1)

        # just in case we got leading 0s continuing the addition
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]
