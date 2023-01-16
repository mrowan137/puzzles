"""
Runtime: 128 ms, faster than 26.04% of Python3 online submissions for Combination Sum.
Memory Usage: 14.4 MB, less than 52.64% of Python3 online submissions for Combination Sum.
"""
# stack -- O((N+1)**M) where M is number of candidates, and N is the
#          target/min(candidates) s.t. N+1 the number of partitions
#          we could generating the each combination.  we choosed the
#          partitions, and basically generated all the partition, to
#          ignore those one that's not work.
class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        # target, partial sum, idx of candidate
        todo = [[target, 0, []]]
        res = []
        while todo:
            t, i, partial = todo.pop()
            n = 0
            while i < len(candidates) and n * candidates[i] <= t:
                if n * candidates[i] == t:
                    res.append(partial + [candidates[i]] * n)
                else:
                    todo.append(
                        [
                            t - n * candidates[i],
                            i + 1,
                            partial + [candidates[i]] * n,
                        ]
                    )
                n += 1

        return res
