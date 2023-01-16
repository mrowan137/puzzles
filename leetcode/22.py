"""
Runtime: 28 ms, faster than 94.92% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.6 MB, less than 67.08% of Python3 online submissions for Generate Parentheses.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Recursion, backtracking
        res = []

        # use n_left, n_right to track number of placed l and r parens
        # we can place a left if still have parens to place
        # we can place a right if fewer right than left
        def helper(parens, n_left, n_right):
            if len(parens) == 2 * n:
                res.append(parens)
            if n_left < n:
                # explore the possibilities with ...(
                parens += "("
                helper(parens, n_left + 1, n_right)
                parens = parens[:-1]
            if n_right < n_left:
                # back up, explore the possibilities with ...)
                parens += ")"
                helper(parens, n_left, n_right + 1)

        helper("", 0, 0)

        return res
