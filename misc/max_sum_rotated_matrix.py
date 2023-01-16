def MaxSumRotated(matrix, a, b):
    """
    Find the max sum of 45 degree rotated matrix
    """
    # 1. create a new matrix big enough to embed input matrix
    # 2. fill in the new elements
    # 3. loop through all rectangles in the new matrix,
    #    take the max sum
    #
    # Let's remember rotations:
    #
    # [ x ]       [  cos t  sin t ] [ x ]
    # [   ] --> k*[               ] [   ]
    # [ y ]       [ -sin t  cos t ] [ y ]
    #
    # t = 45 deg and k = sqrt(2) gives rot matrix of
    #
    # [  1  1 ]
    # [ -1  1 ]
    #
    # so x --> x' = x + y, y -> y' = -x + y + n
    #
    # and we make a constant offset n to make y' g.t. 0

    # size of the input matrix
    M, N = len(matrix[0]), len(matrix)

    # embed the rotated matrix in a square that's big enough
    Mp, Np = M + N - 1, M + N - 1
    rotated_matrix = [
        [float("-inf") for _ in range(M + N - 1)] for _ in range(M + N - 1)
    ]

    # rotate the input matrix
    for i in range(M):
        for j in range(N):
            rotated_matrix[-i + j + (M - 1)][i + j] = matrix[j][i]

    # go through the a x b, b x a matrices and take max sums
    res = float("-inf")
    for i in range(Mp):
        for j in range(Np):
            ii_max = i + 2 * (a - 1)
            jj_max = j + 2 * (b - 1)

            # compute max sum for a x b
            if ii_max < Mp and jj_max < Np:
                s = 0
                for ii in range(i, ii_max + 1):
                    for jj in range(j, jj_max + 1):
                        s += (
                            rotated_matrix[jj][ii]
                            if (rotated_matrix[jj][ii] != float("-inf"))
                            else 0
                        )

                # we calculated a sum for entirely valid rectangle
                res = max(res, s)

            # compute max sum for b x a
            # similar to above, but ii & jj swapped in rot'd idx-ing
            if jj_max < Mp and ii_max < Np:
                s = 0
                for ii in range(i, ii_max + 1):
                    for jj in range(j, jj_max + 1):
                        s += (
                            rotated_matrix[ii][jj]
                            if (rotated_matrix[ii][jj] != float("-inf"))
                            else 0
                        )

                # we calculated a sum for entirely valid rectangle
                res = max(res, s)

    print("The original matrix: \n")
    for row in matrix:
        print("".join(["{:2} ".format(x) for x in row]))
    print("\nThe rot'd matrix: \n")
    for row in rotated_matrix:
        print("".join(["{:4} ".format(x) for x in row]))
    print("The max sum is: {}".format(res))


if __name__ == "__main__":
    # one test problem
    matrix = [[1, 3, 0, 10], [3, 4, 0, 4], [1, 2, 3, 1]]
    MaxSumRotated(matrix, 3, 2)
