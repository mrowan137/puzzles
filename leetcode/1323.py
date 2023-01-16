"""
Runtime: 57 ms, faster than 10.75% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 13.7 MB, less than 99.67% of Python3 online submissions for Maximum 69 Number.
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        i = -1
        num_cpy = num
        j = 0
        while num_cpy:
            num_cpy, rem = divmod(num_cpy, 10)
            if rem == 6:
                i = j
            j += 1

        print(num, i, 10 ** i)
        return num + int(3 * 10 ** i)


"""
Runtime: 50 ms, faster than 20.92% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 13.9 MB, less than 94.18% of Python3 online submissions for Maximum 69 Number.
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        # change the most significant 6 to a 9
        i = str(num).find("6")
        return int(str(num)[:i] + "9" + str(num)[i + 1 :]) if i != -1 else num
