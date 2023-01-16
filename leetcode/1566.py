"""
Runtime: 60 ms, faster than 25.51% of Python3 online submissions for Detect Pattern of Length M Repeated K or More Times.
Memory Usage: 13.9 MB, less than 95.36% of Python3 online submissions for Detect Pattern of Length M Repeated K or More Times.
"""


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        sz = len(arr)
        cnt = 0  # the number of characters in the current sequence
        for i in range(sz - m):  # for each possible
            if arr[i] != arr[i + m]:
                cnt = 0
            else:
                cnt += 1

            if cnt + m == m * k:
                # checked the m elements beyond counted ones match the pattern
                return True

        return False


"""
Runtime: 66 ms, faster than 18.26% of Python3 online submissions for Detect Pattern of Length M Repeated K or More Times.
Memory Usage: 13.9 MB, less than 95.36% of Python3 online submissions for Detect Pattern of Length M Repeated K or More Times.
"""


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        sz = len(arr)
        max_count = float("-inf")

        # for each possible starting position of the pattern
        for i in range(sz - m * k + 1):
            pattern = arr[i : i + m]
            count = 0
            start, end = i, i + m
            while end <= sz and pattern == arr[start:end]:
                count += 1
                start, end = start + m, end + m

            max_count = max(max_count, count)

        return max_count >= k
