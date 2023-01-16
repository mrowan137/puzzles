"""
You are spectating a programming contest with N competitors, each trying to
independently solve the same set of programming problems. Each problem has a
point value, which is either 1 or 2. On the scoreboard, you observe that the ith
competitor has attained a score of S_i, which is a positive integer equal to the
sum of the point values of all the problems they have solved. The scoreboard
does not display the number of problems in the contest, nor their point values. 
Using the information available, you would like to determine the minimum
possible number of problems in the contest.
"""
from typing import List


def getMinProblemCount(N: int, S: List[int]) -> int:
    num1s, num2s = max(S) % 2, max(S) // 2

    # if num1s == 0: num1s = any([s%2 == 1 for s in S])
    for s in S:
        if s % 2 == 1:
            num1s = 1
            break

    return num1s + num2s
