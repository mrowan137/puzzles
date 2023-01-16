"""
Runtime: 44 ms, faster than 51.47% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.1 MB, less than 21.74% of Python3 online submissions for Fizz Buzz.
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = ["" for i in range(n)]
        for i in range(3, max(3, n + 1), 3):
            ans[i - 1] += "Fizz"
        for i in range(5, max(5, n + 1), 5):
            ans[i - 1] += "Buzz"
        for i in range(len(ans)):
            if not ans[i]:
                ans[i] = str(i + 1)

        return ans
