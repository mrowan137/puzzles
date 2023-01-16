"""
A positive integer is considered uniform if all of its digits are equal. For
example, 222222 is uniform, while 223223 is not. Given two positive integers A
and B, determine the number of uniform integers between A and B, inclusive.
"""

from math import log10


def generateUniformIntegers(dA, dB):
    uniformIntegers = []
    for i in range(dA, dB + 1):
        uniformInteger = sum([10 ** n for n in range(i)])
        for j in range(1, 10):
            uniformIntegers.append(uniformInteger)
            uniformInteger += sum([10 ** n for n in range(i)])

    return uniformIntegers


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # generate all uniform integers with len(A) digits to len(B) digits,
    # and check it's between those
    dA, dB = int(log10(A)) + 1, int(log10(B)) + 1
    uniformIntegers = generateUniformIntegers(dA, dB)
    res = 0
    for u in uniformIntegers:
        res += A <= u and u <= B

    return res
