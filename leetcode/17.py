"""
Runtime: 57 ms, faster than 7.41% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.5 MB, less than 30.84% of Python3 online submissions for Letter Combinations of a Phone Number.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        arrs = [d[num] for num in digits]
        print(arrs)
        # construct cross product from arrs
        # ['a','b','c'], ['d', 'e', 'f']
        # want to produce all pairs of length 2
        # take one from first, one from second
        def f(arr):
            # returns list cross products of length n-1
            if len(arr) == 1:
                return arr[0]

            cross_products = f(arr[1:])
            res = []
            for x in arr[0]:
                for c in cross_products:
                    res.append(x + c)

            return res

        return f(arrs)
