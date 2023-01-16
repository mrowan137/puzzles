"""
A photography set consists of N cells in a row, numbered from 1 to N in order,
and can be represented by a string C of length N. Each cell i is one of the
following types (indicated by C_i, the ith character of C):
* If C_i = “P”, it is allowed to contain a photographer
* If C_i = “A”, it is allowed to contain an actor
* If C_i = “B”, it is allowed to contain a backdrop
* If C_i = “.”, it must be left empty

A photograph consists of a photographer, an actor, and a backdrop, such that
each of them is placed in a valid cell, and such that the actor is between the
photographer and the backdrop. Such a photograph is considered artistic if the
distance between the photographer and the actor is between XX and YY cells
(inclusive), and the distance between the actor and the backdrop is also between
XX and YY cells (inclusive). The distance between cells ii and jj is |i - j|∣i−j∣
(the absolute value of the difference between their indices).
"""


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # find PAB, BAP subsequence with requirement j-i and k-j on [x,y]
    #      ijk
    # brute force: for each A, look for [x,y] distance away. count artistic photos.
    res = 0
    for j in range(N):
        if C[j] == "A":
            photos = [
                C[i] + C[j] + C[k] if i >= 0 and k <= N - 1 else "###"
                for i in range(j - Y, j - X + 1)  # fix idx
                for k in range(j + X, j + Y + 1)
            ]

            res += sum([p == "PAB" or p == "BAP" for p in photos])

    return res
