"""
Alternate approach

We want to count number of substrings that differ by exactly one char

abcd
abce

The question is how to count it?
Let count(i, j) denote we count up for the configuration where we align s[i] to t[j].

i=1, j=2
i:   0 1 2 3
     a b c d
j: 0 1 2 3
   a b c e

Essentially, we 'slide' s past t and count substrings differing by one for that config.
And we must write a count function count(i, j).
We can consier a case like
X X X X A X X A
       +5
X X X X B X X B
0+0+0+0+4+4+4+2 
How to count this? 
1. Tally the identical chars.
2. Iterate until finding the first different char.
3. Now for each of those identical chars, we contribute a string differs by one.
4. Until we hit a new different character, then there's a new tally of identicals.
So constantly increment res by prev, which track the prev length of identical chars.
Can tally the current number of identicals with curr;
When hit different, prev = curr.

Why is this so much better than if we enumerate and compare all possible substrings?
Brute force: O( ( 1 + 2 + ... + N)*N( ~ O(N*N*(N-1)/2) ~ O(N^3)
Slide method: O( (M+N)*N) ~ O(N^2)
In brute force case, we enumerate all possible substrings (O(N^2)) and compare to all 
possible substrings in the other (O(N) at worst).
In other approach, we enumerate all posible relative offsets, i.e. sliding the strings
past one another (O(M+N)), and for each possible configuration count strings that 
differ by one (O(N), single pass).
The O(N^3) approach will actually 'overcount' in the sense of continue tally when
we shouldn't bother with it; but slide approach escapes this by skipping those enumeration
/ exploration.  For example:

Compare ABC vs ABD:
ABC enumerations  |  Compare to DEF substring
     A               D, E, F
     AB              DE, EF
     ABC             DEF
     B               D, E, F
     BC              DE, EF
     C               D, E, F
But with slide:
   ABC         C | D
     DEF       

   ABC         B | D, C | E
    DEF      

   ABC         ABC | DEF
   DEF
 ...

See how the slide approach would compare BD then not bother with BC | DE because
it already knows B and D differ.  
So the slide approach encapsulates previous structure/information gathered 
('dynamic programming') to avoid useless comparisons.
"""

"""
Runtime: 2467 ms, faster than 6.92% of Python3 online submissions for Count Substrings That Differ by One Character.
Memory Usage: 14.2 MB, less than 87.54% of Python3 online submissions for Count Substrings That Differ by One Character.
"""


class Solution:
    def differsByOne(self, s1, s2):
        if len(s1) != len(s2):
            return False

        i, strikes = 0, 0
        while strikes < 2 and i < len(s1):
            strikes += s1[i] != s2[i]
            i += 1

        return strikes == 1

    def countSubstrings(self, s: str, t: str) -> int:
        if len(s) > len(t):
            return self.countSubstrings(t, s)

        res = 0
        for i in range(len(s)):
            for j in range(len(s) - i):
                sub_s = s[i : i + j + 1]
                for k in range(len(t)):
                    sub_t = t[k : k + j + 1]
                    res += self.differsByOne(sub_s, sub_t)

        return res
