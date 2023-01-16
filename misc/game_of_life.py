"""Make frames for Conway's Game of Life"""
import numpy as np
import matplotlib.pyplot as plt


def gameOfLife(board):
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
                val = -1  # was alive, now dead (underpop)
            elif cnt <= 3:
                val = 1  # was alive, now alive (happy)
            elif cnt > 3:
                val = -1  # was alive, now dead (overpop)
        else:
            if cnt == 3:
                val = -2  # was dead, now alive (reproduction)
            else:
                val = 2  # was dead, now dead (stay dead)

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


def init(board):
    M, N = len(board[0]), len(board)
    for i in range(M):
        for j in range(N):
            board[j][i] = np.random.choice([0, 1])


def plot(board, tag=""):
    M, N = len(board[0]), len(board)
    xcoord, ycoord = np.arange(M), np.arange(N)

    # plt.cla()
    plt.pcolormesh(xcoord, ycoord, board, cmap="Greys_r")
    plt.draw()
    plt.savefig("./board_" + tag + ".png")


def main():
    # Initialization
    steps = 300  # steps to evolve
    M, N = 500, 500  # size of the board
    board = [[0] * M for _ in range(N)]

    # Initialize to random values
    init(board)

    # Initialize plotting
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    ax.axis("off")

    # Remove margin
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    plt.gca().set_aspect("equal")

    for s in range(steps):
        # Step to the next board state
        gameOfLife(board)

        # Plot
        plot(board, str(s).zfill(3))


if __name__ == "__main__":
    main()
