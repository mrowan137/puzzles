"""
Runtime: 51 ms, faster than 26.99% of Python3 online submissions for Game of Life.
Memory Usage: 14.4 MB, less than 41.57% of Python3 online submissions for Game of Life.
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board[0]), len(board)
        # Rules (N neighbors):
        # 1. live cell
        #     - N < 2     dies
        #     - N > = 2,3 lives
        #     - N > 3     dies
        # 2.  dead cell
        #     - N = 3     lives
        # Every cell has a value 1 or 0 and can move to 1 or 0
        # So we could encode to 0,1,2,3
        # (dead )  0  0 0 --> 0 (00)
        # (alive)  1  1 0 --> 1 (01)
        # (dead )  2  0 1 --> 2 (10)
        # (alive)  3  1 1 --> 3 (11)
        # Note v % 2 == 0 --> dead, v % 2 == 1 --> alive
        # so steps is: encode according to neighbors
        # decode
        def neighbors(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            nbrs = [
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            ]
            res = 0
            for nbr in nbrs:
                dx, dy = nbr
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue
                res += board[y][x] % 2

            return res

        def encode(i, j):
            # according to number of neighbors, get the encoded value
            nbrs = neighbors(i, j)
            if board[j][i] % 2 == 1:
                if nbrs < 2:
                    return 1
                elif nbrs == 2 or nbrs == 3:
                    return 3
                elif nbrs > 3:
                    return 1
            elif board[j][i] % 2 == 0:
                if nbrs == 3:
                    return 2
                else:
                    return 0

        def decode(i, j):
            return 1 if board[j][i] > 1 else 0

        for i in range(m):
            for j in range(n):
                board[j][i] = encode(i, j)

        for i in range(m):
            for j in range(n):
                board[j][i] = decode(i, j)


"""
Runtime: 36 ms, faster than 51.41% of Python3 online submissions for Game of Life.
Memory Usage: 14.1 MB, less than 97.14% of Python3 online submissions for Game of Life.
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we think up an encoding
        #  1: now 1, next 1
        # -1: now 1, next 0
        #  2: now 0, next 0
        # -2: now 0, next 1
        # use like: abs(v) == 1: neighbor is now 1
        #           abs(v) == 2: neighbor is now 0
        M, N = len(board[0]), len(board)

        # update according to rules
        def update_encoded(i, j):
            neighbors = (
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (-1, 0),
                (-1, 1),
            )

            # count the number of neighbors
            cnt = 0
            legal = lambda i, j: i >= 0 and i < M and j >= 0 and j < N
            for n in neighbors:
                dx, dy = n
                if legal(i + dx, j + dy) and abs(board[j + dy][i + dx]) == 1:
                    cnt += 1

            # encode the new entry
            alive = board[j][i]
            if alive:
                if cnt < 2:
                    val = -1  # was alive, now dead  (underpop)
                elif cnt <= 3:
                    val = 1  # was alive, now alive (happy)
                elif cnt > 3:
                    val = -1  # was alive, now dead  (overpop)
            else:
                if cnt == 3:
                    val = -2  # was dead, now alive    (reproduction)
                else:
                    val = 2  # was dead, now dead     (stay dead)

            board[j][i] = val

        def decode(i, j):
            # convert from our encoding scheme to 0s and 1s
            if board[j][i] in (-1, 2):
                board[j][i] = 0
            elif board[j][i] in (1, -2):
                board[j][i] = 1

        # Update the grid in place
        for i in range(M):
            for j in range(N):
                update_encoded(i, j)

        for i in range(M):
            for j in range(N):
                decode(i, j)

        return board
