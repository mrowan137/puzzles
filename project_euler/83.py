"""
Q: In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in bold red and
is equal to 2297.

  **131**   673   **234** **103**   **18**
  **201**  **96** **342**   965    **150**
    630     803     746   **422**  **111**
    537     699     497   **121**    956
    805     732     524    **37**  **331**

Find the minimal path sum from the top left to the bottom right by by moving
left, right, up, and down in matrix.txt, a 31K text file containing an 80 by 80
matrix.

A: 425185
"""


def dfs(start, end, matrix, seen, memo):
    if tuple(seen) in memo:
        return memo[tuple(seen)]
    # return minimal path sum meeting following conditions:
    #   1. start at `start`
    #   2. end at `end`
    #   3. path not crossing back on itself
    #
    # recursive approach blows up stack space, iterative
    # approach (below) to externalize the stack
    rows, cols = len(matrix), len(matrix[0])
    i, j = start
    start_is_legal = 0 <= i < rows and 0 <= j < cols

    if not start_is_legal or start in seen:
        memo[(s for s in seen)] = float("inf")
        return float("inf")

    seen.append(start)

    if start == end:
        seen.pop(-1)
        return matrix[i][j]

    neighbors = [
        (i + di, j + dj) for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ]

    res = matrix[i][j] + min(
        dfs(nbr, end, matrix, seen, memo) for nbr in neighbors
    )

    memo[(s for s in seen)] = res

    seen.pop(-1)

    return res


def iterate(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end, path_sum = (0, 0), (rows - 1, cols - 1), 0
    queue = [(start, path_sum, set())]
    min_path_sum = float("inf")

    smallest_path_sum_so_far = [
        [float("inf") for _ in range(cols)] for _ in range(rows)
    ]

    while queue:
        start, path_sum, seen = queue.pop()
        i, j = start
        start_is_legal = 0 <= i < rows and 0 <= j < cols

        if not start_is_legal or start in seen:
            continue

        seen.add(start)

        if start == end:
            min_path_sum = min(min_path_sum, path_sum + matrix[i][j])
            continue

        # no need to continue if current path sum is larger
        if path_sum + matrix[i][j] > smallest_path_sum_so_far[i][j]:
            continue

        smallest_path_sum_so_far[i][j] = min(
            smallest_path_sum_so_far[i][j], path_sum + matrix[i][j]
        )

        neighbors = [
            (i + di, j + dj) for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ]
        for nbr in neighbors:
            if not nbr in seen:
                queue.append(
                    (nbr, matrix[i][j] + path_sum, set(s for s in seen))
                )

    return min_path_sum


def minimum_path_sum(file_name):
    # read file
    matrix = []
    with open(file_name, "r", encoding="utf-8") as matrix_file:
        for line in matrix_file:
            row = line.replace("\n", "").split(",")
            matrix.append([int(x) for x in row])

    # Test case; expect 2297
    # matrix = [
    #     [131, 673, 234, 103, 18],
    #     [201, 96, 342, 965, 150],
    #     [630, 803, 746, 422, 111],
    #     [537, 699, 497, 121, 956],
    #     [805, 732, 524, 37, 331],
    # ]

    # this exceeds recursion depth with full problem:
    # seen, memo = [], {}
    # rows, cols = len(matrix), len(matrix[0])
    # res = dfs( (0, 0), (rows-1, cols-1), matrix, seen, memo)

    # iterative rewrite of recursive:
    res = iterate(matrix)

    return res


if __name__ == "__main__":
    MATRIX_FILE = "./matrix_p83.txt"
    print(f"Minimum path sum: {minimum_path_sum(MATRIX_FILE)}")
