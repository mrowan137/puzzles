"""
Runtime: 555 ms, faster than 43.89% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 16.3 MB, less than 52.88% of Python3 online submissions for Longest Increasing Path in a Matrix.
"""
# recursion with memo -- O(MN)
# now each is calculated only once, leading to O(MN)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix[0]), len(matrix)

        def find_the_longest_path(i, j, memo, seen=None):
            if (i, j) in memo:
                return memo[(i, j)]

            neighbors = ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))
            res = 1
            for n in neighbors:
                nx, ny = n

                # each neighbor want their own track
                seen = set()
                if nx < M and nx >= 0 and ny < N and ny >= 0:
                    # if it's a valid square,
                    if not (nx, ny) in seen and matrix[j][i] < matrix[ny][nx]:
                        # if it's part of a valid sequence,
                        seen.add((i, j))  # let my descendant know where I was..
                        res = max(
                            res, 1 + find_the_longest_path(nx, ny, memo, seen)
                        )
            memo[(i, j)] = res
            return res

        m = float("-inf")
        memo = {}
        for i in range(M):
            for j in range(N):
                m = max(m, find_the_longest_path(i, j, memo))

        return m


"""
TLE
"""
# iteration -- O(2^(M+N))
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix[0]), len(matrix)

        def find_the_longest_path(i0, j0):
            s0 = set()
            l0 = 1
            res = 1
            todo = [[i0, j0, s0, l0]]
            while todo:
                i, j, seen, l = todo.pop()
                neighbors = ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))
                for n in neighbors:
                    nx, ny = n
                    my_seen = set([el for el in seen])
                    # each neighbor want their own track
                    if nx < M and nx >= 0 and ny < N and ny >= 0:
                        # if it's a valid square,
                        if (
                            not (nx, ny) in my_seen
                            and matrix[j][i] < matrix[ny][nx]
                        ):
                            # if it's part of a valid sequence,
                            my_seen.add(
                                (i, j)
                            )  # let my descendant know where I was..
                            todo.append([nx, ny, my_seen, l + 1])
                            res = max(res, l + 1)
            return res

        m = float("-inf")
        for i in range(M):
            for j in range(N):
                m = max(m, find_the_longest_path(i, j))

        return m


"""
TLE
"""
# recursion -- O(2^(M+N))
# in the worst case, each search along M and N directions
# spawns 2 others, leading to 2^M * 2^N = 2^(M+N) calls
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix[0]), len(matrix)

        def find_the_longest_path(i, j, seen=None):
            neighbors = ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))
            res = 1
            for n in neighbors:
                nx, ny = n

                # each neighbor want their own track
                seen = set()
                if nx < M and nx >= 0 and ny < N and ny >= 0:
                    # if it's a valid square,
                    if not (nx, ny) in seen and matrix[j][i] < matrix[ny][nx]:
                        # if it's part of a valid sequence,
                        seen.add((i, j))  # let my descendant know where I was..
                        res = max(res, 1 + find_the_longest_path(nx, ny, seen))

            return res

        m = float("-inf")
        for i in range(M):
            for j in range(N):
                m = max(m, find_the_longest_path(i, j))

        return m
