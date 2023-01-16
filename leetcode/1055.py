"""
Runtime: 192 ms, faster than 5.14% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 14.8 MB, less than 6.90% of Python3 online submissions for Shortest Way to Form String.
"""
# O(N) and using a clever array to precompute the index we would need
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        M, N = len(source), len(target)

        # this is a map from letter and idx in source, to the subsequent idx
        idx = {chr(ord("a") + i): [0] * M for i in range(26)}

        # when we hit the ith letter in source, the next idx is i + 1
        for i in range(M):
            idx[source[i]][i] = i + 1

        # fill in the table letter by letter, drag from the end of source
        # this tells us that for a given index j into source, and we
        # given a letter in target, which one should we use? e.g.
        # source = abcdefg
        # idx['d'] = [4, 4, 4, 4, 0, 0, 0]
        # idx['e'] = [5, 5, 5, 5, 5, 0, 0]
        # tells us that for j <= 3, 'd' will make j will jump to 4
        # tells us that for j <= 4, 'e' will make j jump to 5
        for i in range(26):
            pre = 0  # track the last idx we saw
            for j in range(M - 1, -1, -1):
                if idx[chr(ord("a") + i)][j] == 0:
                    idx[chr(ord("a") + i)][j] = pre
                else:
                    pre = idx[chr(ord("a") + i)][j]

        res = 1
        i = j = 0
        while i < len(target):
            if j == len(source):
                # restart, we use a copy
                j = 0
                res += 1

            if idx[target[i]][0] == 0:
                # it means we hit a letter that i not in source because
                # we did not overwrite the initial value in the table
                return -1

            # get the next idx
            j = idx[target[i]][j]
            if j == 0:
                # j was not at the end, but we will not use the rest of
                # letter in source; so jump back j to 0; decrement i
                # because we did not use target[i]
                res += 1
                i -= 1

            i += 1

        return res


"""
Runtime: 68 ms, faster than 36.40% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 14.4 MB, less than 16.78% of Python3 online submissions for Shortest Way to Form String.
"""
# O(N log M)
# still iterating through target and (repeatedly) source,
# but instead of linearly searching through M for matches,
# store the indices of appearance beforehand, and look for
# one that is at or beyond the current j.  when we find a
# value beyond the current j, we need to use a new copy of source.
import bisect


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        M, N = len(source), len(target)
        res = 1

        # map from letter to index of appearance within source
        idx = {chr(ord("a") + i): [] for i in range(26)}
        for i in range(M):
            idx[source[i]].append(i)

        i = 0  # to track index within target
        j = 0  # to track index within source

        # go through the target
        while i < N:
            # this is the list of candidate indices
            # where target[i] appears in source
            tar = idx[target[i]]

            # exit if there are no appearances of target letter in source
            if not tar:
                return -1

            # from the candidate indices (those with correct value, target[i])
            # find the first greater or equal to current idx j in source
            k = bisect.bisect_left(tar, j)

            if k == len(tar):
                # the letter appears, but we passed them all. restart.
                res += 1
                j = 0
            else:
                # we found the letter, so use it
                j = tar[k] + 1
                i += 1

        return res


"""
Runtime: 61 ms, faster than 43.03% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 14.2 MB, less than 65.36% of Python3 online submissions for Shortest Way to Form String.
"""
# O(M*N), but with no set
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # two pointer, greedy
        M, N = len(source), len(target)

        res = 0
        j = 0

        # as long as there's target leters to process,
        while j < N:
            j0 = j
            for i in range(M):
                # iterate through source repeatedly,
                # pushing along target index as we get matches
                if j < N and target[j] == source[i]:
                    j += 1

            # if the target index did not move, we exit
            if j == j0:
                return -1

            # otherwise, we used some source subsequence and increment
            res += 1

        return res


"""
Runtime: 1841 ms, faster than 5.15% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 14.3 MB, less than 38.13% of Python3 online submissions for Shortest Way to Form String.
"""
# O(M*N)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # two pointer, greedy
        M, N = len(source), len(target)

        i, j = 0, 0
        res = 0

        while j < N:
            if target[j] not in set(source):
                # cannot be formed from source
                return -1

            if source[i] == target[j]:
                # find a match, increment
                i += 1
                j += 1

            else:
                # no match
                i += 1

            if i == M:
                # reached the end of the source
                i = 0
                res += 1

        # if i is in the middle of source, we used one more instance of source
        return res + int(i != 0)
