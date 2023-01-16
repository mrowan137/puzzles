"""
You're trying to open a lock. The lock comes with a wheel which has the integers
from 1 to N arranged in a circle in order around it (with integers 1 and N
adjacent to one another). The wheel is initially pointing at 1.
"""
from typing import List


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # give the shortest time to enter the combo, given lock with N numbers

    # start at 1
    curr = 1
    res = 0

    for d in C:
        res += min((d - curr) % N, (curr - d) % N)
        curr = d

    return res
