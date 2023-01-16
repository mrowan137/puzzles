"""
Runtime: 907 ms, faster than 51.16% of Python3 online submissions for Wildcard Matching.
Memory Usage: 22.5 MB, less than 57.07% of Python3 online submissions for Wildcard Matching.

dp O(len(s)*len(p)).  the brute force TLE below get to O(N^3) because we loop
over the dp, and when p hits a *, we need to loop back over things we already
calculated in s to see if there's a match.  instead it will be better if we could
loop over the pattern, and fill out the string part of dp in one go.

Concrete example, fill out the dp below row by row.
Hit a star requires looks for the first match in the preceding row,
then jump to the * row and sets remaining elements to T --> O(N^2).
so we could bump into a * max of len(p) times, but each one only take O(N)
to fill out the row.
   a b c
 a T F F
 b F T F
 * F T T

Now loop the other way, the star requires to back up a column, and check
the rows for a match --> O(N^3).  so iterating this way requires each *
to iterate through s looking O(N) for a match substrings. and there could be O(N^2)
times we bump into a *, each iterating through s -->O(N^3).
   a b *
 a T F F
 b F T T
 c F F T
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s and not p:
            return False

        # multiple c of * to replace by a single
        i = 0
        while i < len(p) - 1:
            if p[i] == "*" and p[i + 1] == "*":
                p = p.replace("**", "*")
            else:
                i += 1

        if not s:
            if p in ["*", ""]:
                return True
            else:
                return False

        szp, szs = len(p), len(s)
        dp = [[False] * (szp + 1) for _ in range(szs + 1)]

        # the empty string match
        dp[0][0] = True

        for i in range(1, szp + 1):
            if p[i - 1] == "*":
                # back up in pattern, find the first match
                m = 0
                while m < szs + 1 and dp[m][i - 1] == False:
                    m += 1
                while m < szs + 1:
                    dp[m][i] = True
                    m += 1
            elif p[i - 1] == "?":
                for j in range(1, szs + 1):
                    # match if preceding strings match
                    dp[j][i] = dp[j - 1][i - 1]
            else:  # letter
                for j in range(1, szs + 1):
                    # match if letters match, and preceding string match
                    dp[j][i] = p[i - 1] == s[j - 1] and dp[j - 1][i - 1]

        # return if they match as last
        return dp[-1][-1]


"""
Runtime: 452 ms, faster than 81.08% of Python3 online submissions for Wildcard Matching.
Memory Usage: 22.4 MB, less than 62.52% of Python3 online submissions for Wildcard Matching.

dp[p][s] represents a match considering up to [0, p+1], [0, s+1]
where p and s are pointers into pattern and string
Cases:
    (s, p) = (letter, letter)
        dp[p][s] = dp[p-1][s-1] == True and string[s] == pattern[s]
    (s, p) = (letter, ?)
        dp[p][s] = dp[p-1][s-1] == True
    (s, p) = (letter, *)
        dp[p][s] --> find the first match 'sss' 'ppp',
                     by iteration over s (call the match idx m)
                     then 'ppp*' matches string from m onward

O(s*p) to iterate over dp array
"""


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        string = "#" + string
        pattern = "#" + pattern
        sz_p = len(pattern)
        sz_s = len(string)

        dp = [[False] * (sz_s) for _ in range(sz_p)]
        dp[0][0] = True

        for p in range(1, sz_p):
            if pattern[p] == "*":
                # move before * and find first match wrt s
                m = 0
                while m < sz_s and dp[p - 1][m] == False:
                    m += 1

                # if we found a match, i.e. d[p-1][m] = True,
                # then we star will swallow all chars beyond m,
                # and set dp[p][m:]
                #     a b c d e f _ _ _ _
                #     a b c d *
                #     0 1 2 3 4 5 6 7 8 9
                #           m p
                while m < sz_s:
                    dp[p][m] = True
                    m += 1

            elif pattern[p] == "?":
                for s in range(1, sz_s):
                    dp[p][s] = dp[p - 1][s - 1]

            else:  # letter
                for s in range(1, sz_s):
                    dp[p][s] = dp[p - 1][s - 1] and pattern[p] == string[s]

        return dp[-1][-1]


"""
Runtime: 40 ms, faster than 98.85% of Python3 online submissions for Wildcard Matching.
Memory Usage: 14.4 MB, less than 84.09% of Python3 online submissions for Wildcard Matching.

O(s*logp) in the average case (see https://arxiv.org/pdf/1407.0950.pdf)
O(s*p) worst case
"""


class Solution:
    def isMatch(self, string, pattern) -> bool:
        sz_p, sz_s = len(pattern), len(string)

        # pointers into string and pattern
        s = p = 0

        # pointers to star location and string chars after star to skip
        skip_to = star = -1

        while s < sz_s:
            # if pattern not used up
            # and chars match or '?', increment
            if p < sz_p and pattern[p] in [string[s], "?"]:
                s += 1
                p += 1

            # if pattern not used up and pattern hits a star,
            # try matching assuming '*' eats 0 chars
            elif p < sz_p and pattern[p] == "*":
                star = p
                p += 1
                skip_to = s

            # if run out of match and we did not see a star previously
            elif star == -1:
                return False

            # if run out of match and we did see a star previously
            else:
                skip_to += 1
                s = skip_to
                p = star + 1

        # we matched everything in string, remaining pattern chars
        # can only be star
        return pattern[p:] == "*" * (sz_p - p)


"""
Runtime: 1160 ms, faster than 15.15% of Python3 online submissions for Wildcard Matching.
Memory Usage: 665 MB, less than 9.14% of Python3 online submissions for Wildcard Matching.

recursion and memoization
we can have at most s*p non-memoized calls;
each non-memoized called takes s+p time to create
hash and substrings s[1:], p[1:] to pass to helper;
altogether, time is P(s*p*(s+p))
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def remove_dup(p: str) -> str:
            if not p:
                return ""
            p_new = p[0]
            for i in range(1, len(p)):
                # if char is a star
                if p[i] != "*":
                    p_new += p[i]
                # char is not a star
                else:
                    # if there was a star previously
                    if p[i] == p[i - 1]:
                        pass
                    # else if there was not a star previously
                    else:
                        p_new += "*"
            return p_new

        def helper(s: str, p: str, memo: dict) -> (str, str):
            if (s, p) in memo.keys():
                return memo[(s, p)]

            # if strings match or p is a wild
            if s == p or p == "*":
                memo[(s, p)] = True

            # else if no match and we hit the end of string or pattern;
            # note we remove dup '*' so remaining p chars cannot be '*'
            elif s == "" or p == "":
                memo[(s, p)] = False

            # else if current chars match or pattern has '?' next;
            # note the string and pattern are nonempty, by prev
            elif s[0] == p[0] or p[0] == "?":
                memo[(s, p)] = helper(s[1:], p[1:], memo)

            # wildcard case; '*' can swallow a string char, or move past star char
            elif p[0] == "*":
                memo[(s, p)] = helper(s[1:], p, memo) or helper(s, p[1:], memo)

            # string and pattern don't match, no mote '*' to save us
            else:
                memo[(s, p)] = False

            return memo[(s, p)]

        # map from strings to whether they match, to be filled recursively
        memo = {}
        p = remove_dup(p)
        return helper(s, p, memo)


"""
TLE
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s and not p:
            return False

        # multiple c of * to replace by a single
        i = 0
        while i < len(p) - 1:
            if p[i] == "*" and p[i + 1] == "*":
                p = p.replace("**", "*")
            else:
                i += 1

        if not s:
            if p in ["*", ""]:
                return True
            else:
                return False

        szp, szs = len(p), len(s)
        dp = [[False] * (szp + 1) for _ in range(szs + 1)]

        # the empty string match
        dp[0][0] = True

        for j in range(szs + 1):
            for i in range(1, szp + 1):
                dp[j][i] = (
                    (
                        p[i - 1] == s[j - 1] and dp[j - 1][i - 1]
                    )  # the current char match and preceding strings match
                    or (
                        p[i - 1] == "?" and dp[j - 1][i - 1]
                    )  # the current char has ? and preceding strings match
                    or (
                        p[i - 1] == "*"
                        and any(dp[k][i - 1] for k in range(j + 1))
                    )  # wildcard eats s string
                )
        # return if they match as last
        return dp[-1][-1]
