"""
Given string s, it is 'good' if split into two nonempty strings p, q where
p+q==s and num distinct letters in p and q is the same. For example,
aabb == aa + bb is good because numDestinct(aa) == numDestinct(bb) == 1. We want
to find the number of 'good' splits. For example, abb has 1 good splits:
a + bb == abb. How to count the good splits?  

Brute force way is iterate through the list and see if that split is good.
# Brute force.  But it's not good enough.
        goodSplit = lambda i: len(set(s[:i])) == len(set(s[i:]))
        return sum(goodSplit(i) for i in range(1,len(s))) 
        
Maybe a better way: have two dict, one for 'left' one for right.
Count initially the number of unique letters in each one.
And 'move' letter from one to the other, changing the count of uniques in each dict.
If the num uniques is the same, add to the finaly tally.

from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2: return 0

        # Init
        l, r = Counter(s[:1]), Counter(s[1:])
        nl, nr = len(l), len(r)
        res = nl == nr
        
        for i in range(1, len(s)-1):
            res += nl == nr
            l[s[i]] += 1
            r[s[i]] -= 1
            nr -= r[s[i]] == 0
            nl += l[s[i]] == 1
                
        return res

Maybe an even better way:
have arrays l, r to track uniques seen to that point.
Do single pass tracking uniques seen, iterating from left and then right.
Then iterate and compare tallies at each entries of the left and right arrays.
O(3*N) ~ O(N) time complexity.

Runtime: 172 ms, faster than 76.98% of Python3 online submissions for Number of Good Ways to Split a String.
Memory Usage: 17.1 MB, less than 5.92% of Python3 online submissions for Number of Good Ways to Split a String.
"""


class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0

        u_l, u_r = set(), set()
        l, r = [0] * (len(s) - 1), [0] * (len(s) - 1)
        for i in range(len(s) - 1):
            j = len(s) - 1 - i - 1
            u_l.add(s[i])
            u_r.add(s[j + 1])

            l[i] = len(u_l)
            r[j] = len(u_r)

        return sum([l[i] == r[i] for i in range(len(s) - 1)])
