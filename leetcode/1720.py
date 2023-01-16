"""
Runtime: 228 ms, faster than 61.48% of Python3 online submissions for Decode XORed Array.
Memory Usage: 15.9 MB, less than 67.78% of Python3 online submissions for Decode XORed Array.
"""


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[-1] ^ encoded[i])

        return res


# first = f, encoded = [a,b,c]
# decode = [w,x,y,z]
# f       = w
# f^x     = a
# f^x^y   = b
# f^x^y^z = c
# Go in reverse:
# c^b = z
# b^a = y
# a^f = x
