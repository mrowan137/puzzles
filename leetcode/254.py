"""
Runtime: 97 ms, faster than 66.36% of Python3 online submissions for Factor Combinations.
Memory Usage: 14.8 MB, less than 76.19% of Python3 online submissions for Factor Combinations.
"""
# iterative
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        todo, res = [(n, 2, [])], []

        while todo:
            # - target is what we want to find factors
            # - product(n_div_by_target_factors) = product(n / target)
            #       the completed part of our lists
            # - i is the smallest factor we are allowed to add;
            #   each thread want to remember that
            target, i, n_div_by_target_factors = todo.pop()
            while i * i <= target:
                if target % i == 0:
                    # we can decompose target
                    # (n/target)*(target/i)*i = n
                    res.append(n_div_by_target_factors + [i, target // i])

                    # add to todo list in case target/i is decomposable
                    todo.append([target // i, i, n_div_by_target_factors + [i]])

                i += 1

        return res


"""
Runtime: 961 ms, faster than 11.01% of Python3 online submissions for Factor Combinations.
Memory Usage: 18.3 MB, less than 5.21% of Python3 online submissions for Factor Combinations.
"""
# O(N^2)
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        memo = {}  # number --> list of the factors
        memo[1] = []

        def helper(n):
            # return list of factor lists
            if n in memo.keys():
                return memo[n]

            res = []

            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    res.append(i)

            # generate those list from the factors
            final = []
            for r in res:
                maybe = helper(n // r)
                if maybe:
                    for x in maybe:
                        add = sorted([r] + x)
                        if not add in final:
                            final.append(add)

                add = sorted([r, n // r])
                if not add in final:
                    final.append(add)

            memo[n] = final
            return final

        return helper(n)
