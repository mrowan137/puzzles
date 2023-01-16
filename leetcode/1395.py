"""
Runtime: 1181 ms, faster than 63.52% of Python3 online submissions for Count Number of Teams.
Memory Usage: 14.4 MB, less than 46.48% of Python3 online submissions for Count Number of Teams.
"""
# Dynamic programming
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # brute force: enumerate all possible teams: O(N^3)
        # But can we do better?
        # Instead of counting every possible team,
        # Consider an individual and ask,
        # "how many teams I can be a part of as middle?"
        # L G G 5 L L G G
        # For 5, we multiply num G after by num L before: O(N^2).
        # There's one more question, how do we know this sum is exhaustive?
        # Consider the list of all teams.
        # The middle number will be one of the set of numbers.
        # So we condition on the middle is one of the numbers,
        # and sum over all possibilities.

        res = 0
        # forward pass
        for i, r in enumerate(rating):
            num_less_b = sum(r_j < r for r_j in rating[:i])
            num_gtr_a = sum(r < r_j for r_j in rating[i:])
            num_less_a = sum(r > r_j for r_j in rating[i:])
            num_gtr_b = sum(r_j > r for r_j in rating[:i])
            res += num_less_b * num_gtr_a + num_less_a * num_gtr_b

        return res


"""
Brute force
Runtime: 2160 ms, faster than 6.47% of Python3 online submissions for Count Number of Teams.
Memory Usage: 14.7 MB, less than 9.95% of Python3 online submissions for Count Number of Teams.
"""


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        sz = len(rating)
        dp2 = [0] * sz

        for i in range(sz):
            dp2[i] = sum([r < rating[i] for r in rating[:i]])
            res += sum([dp2[j] * (rating[j] < rating[i]) for j in range(i)])

        rating = rating[::-1]

        for i in range(sz):
            dp2[i] = sum([r < rating[i] for r in rating[:i]])
            res += sum([dp2[j] * (rating[j] < rating[i]) for j in range(i)])

        return res
