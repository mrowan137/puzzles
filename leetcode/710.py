"""
Runtime: 7293 ms, faster than 5.04% of Python3 online submissions for Random Pick with Blacklist.
Memory Usage: 23.4 MB, less than 83.09% of Python3 online submissions for Random Pick with Blacklist.

create a map from the possible indices to the valid nums.
suppose there's n numbers, and b of them are blacklist.
then there are n - b possibilities of the valid numbers we choose
consider partition the nums along the first n-b, and the remainder
    [ n - b | b ]
and note that however many blacklist nums are in the first part,
there is equal number of good nums in the second part.
so we create a map by iterate over the n-b elements,
and a tracker at n-b that is always at the good element.
"""
import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        b = len(blacklist)
        self.sz = n - b
        # map from a possible idx to one one of the n-b possible nums
        self.m = {}

        g = n - b
        for bad in blacklist:
            if bad < n - b:
                while g in blacklist:
                    g += 1
                self.m[bad] = g
                g += 1
                # point i to the next good idx

    def pick(self) -> int:
        i = random.randint(0, self.sz - 1)
        return self.m[i] if i in self.m.keys() else i


"""
Runtime: 4820 ms, faster than 7.56% of Python3 online submissions for Random Pick with Blacklist.
Memory Usage: 22.6 MB, less than 98.69% of Python3 online submissions for Random Pick with Blacklist.

O(b) initialize, O(1) pick
Notation: Let B = length of the blacklist, W = length of the whitelist.
          wlist, blist are the list themselves.
          Then B + W = N.  We will construct a map [0, W) --> wlist.
          The simple way is to iterate:
              m  = {}
              for i in range(W):
                  if not i in blist:
                      m[i] = i
                  else:
                      m[i] = j
          and we can point j to a number not in the blacklist.
          Note that the number of blacklist numbers in [0, W)
          is equal, by symmetry, to the number of whitelist nums
          on [W, W+B). Complexity to construct this is O(W), but
          can we do better?
          We could go for O(B) solution, to do so we can optimize by
          iterating only over blacklist, and assuming the value of
          the map is i unless it is a blacklist number. If B is in
          the range [0, W), the possible values of 'keys' for the map
          then we map it to a whitelist value from the range [W, W+B)
          for b in blist:
              if b < W: m[b] = j
          where j points to a whitelist number from [W, W+B)

          The ingenious symmetry realization is the following:
          the number of blacklist numbers on [0, W) is equal
          to the number of whitelist numbers on [W, W+B),
          which must be true because there are W whitelist nums in total.

"""
import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.m = {}
        self.w = n - len(blacklist)
        j = self.w
        for b in blacklist:
            if b < self.w:
                while j in blacklist:
                    j += 1
                self.m[b] = j
                j += 1

    def pick(self) -> int:
        k = random.randint(0, self.w - 1)
        return k if not k in self.m.keys() else self.m[k]


"""
Runtime: 524 ms, faster than 21.08% of Python3 online submissions for Random Pick with Blacklist.
Memory Usage: 23.1 MB, less than 90.99% of Python3 online submissions for Random Pick with Blacklist.

There is yet another strategy.
wlist: 0 x x 3 x 5
blist:   1 2   4
idx  : 0     1   2
skip : 0     2   3
We can choose randomly an index from the number of possible wlist nums.
Once doing, it is either valid wlist num (like 0), or we can add a skip
to get to the jth largest wlist num.  To do it fast we can use binary
search to get the largest blist num  smaller than wlist[j].  In this case
wlist[j] = j + skip,
where blist[skip] is the largest blacklist num < wlist[j]
O(B log B) to sort the blacklist
O(log B) to binary search on the blacklist
"""
import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blacklist = sorted(blacklist)

    def pick(self) -> int:
        j = random.randint(0, self.n - len(self.blacklist) - 1)
        lo, hi = 0, len(self.blacklist) - 1

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.blacklist[mid] > j + mid:
                hi = mid - 1
            else:
                lo = mid

        return j + hi + 1 if lo == hi and self.blacklist[hi] - hi <= j else j
