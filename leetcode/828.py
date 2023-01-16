"""
Runtime: 276 ms, faster than 75.23% of Python3 online submissions for Count Unique Characters of All Substrings of a Given String.
Memory Usage: 15.1 MB, less than 57.80% of Python3 online submissions for Count Unique Characters of All Substrings of a Given String.

Insight: count the contributions from each char 
         instead of score of each substring.

  counting score for each substring
  ---------------------------------
    AABAA
    45321

  counting score for each char -- in how many strings am I unique?
  ----------------------------------------------------------------
    AABAA 
    12921

Brute force would be to consider each substring and sum the 'unique' count for
that substring. But an alternate approach, for each char how much could it
contribute to the final tally? In other words, how many strings where char is
unique? Insight is to see the two methods give the same result.
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res = 0

        # track locations of last two seen
        last = {chr(i + 65): [-1, -1] for i in range(26)}

        # sum contribution each char
        for i, c in enumerate(s):
            k, j = last[c]
            res += (i - j) * (j - k)
            last[c] = [j, i]

        # sum the final contribution
        for c in last:
            k, j = last[c]
            res += (len(s) - j) * (j - k)

        return res


"""
Too slow!
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        def countUnique(i):
            res, curr = 0, 0
            seen_1, seen_2 = set(), set()
            for j in range(0, len(s) - i):
                if s[i + j] in seen_2:
                    res += curr
                    continue
                if s[i + j] in seen_1:
                    seen_2.add(s[i + j])
                    curr -= 1
                    res += curr
                    continue
                curr += 1
                res += curr
                seen_1.add(s[i + j])

            return res

        return sum(countUnique(i) for i in range(len(s)))
