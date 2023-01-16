"""
Runtime: 60 ms, faster than 93.51% of Python3 online submissions for Permutation in String.
Memory Usage: 14.5 MB, less than 32.56% of Python3 online submissions for Permutation in String.
"""
# Sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)

        # Make a count array for s1
        s1_cnt = [0] * 26
        for i in range(M):
            s1_cnt[ord(s1[i]) - ord("a")] += 1

        # Make a sliding window
        window = [0] * 26
        j = 0
        for i in range(N):
            window[ord(s2[i]) - ord("a")] += 1
            if i - j >= M:
                window[ord(s2[j]) - ord("a")] -= 1
                j += 1
            if window == s1_cnt:
                return True

        return False


"""
Runtime: 1348 ms (beats 24.39%)
Memory: 14 MB (beats 30.27%)
"""
# Counter
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if M > N:
            return False

        s1_cnt = Counter(s1)
        for i in range(N - M + 1):
            if s1_cnt == Counter(s2[i : i + M]):
                return True

        return False
