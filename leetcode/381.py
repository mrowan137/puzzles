"""
Runtime: 953 ms, faster than 8.99% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 65.7 MB, less than 43.61% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
"""
# how to get O(1) insert and remove? we'll need to use some memory to track locations
# within nums.  then we can overwrite and pop from nums.
import random
from collections import defaultdict

# goal is to make make a datastructure that contains set of numbers, POSSIBLE DUPLICATES
# it needs following operations:
#     insert    : insert number into dataset
#     remove    : remove number from dataset
#     getRandom : get a random number
class RandomizedCollection:
    def __init__(self):
        # nums: list of all  [ val, idx into m[val] ]
        # m   : m[val] gives indices where val appear in nums
        self.nums, self.m = [], defaultdict(list)

    def insert(self, val):
        # true if it was not there already
        result = val not in self.m

        # it add an idx at the end of nums
        self.m[val].append(len(self.nums))

        # it add an idx at the end of m[val]
        self.nums.append([val, len(self.m[val]) - 1])

        return result

    def remove(self, val):
        # true if it is there
        result = val in self.m

        # we're gonna remove a val from nums.
        if result:
            # val, it's gonna get overwrite by last in nums. SAVE IT!
            last = self.nums[-1]

            # where in nums do we put last?
            # we removing val, so it goes to where val was
            # where in nums is val? it's at m[val][-1].
            self.nums[self.m[val][-1]] = last

            # remove that last one, we don't need it
            self.nums.pop()

            # last is moving, we need to update it's idx of appearance
            # m[last val][idx into m[last val]] = idx into nums of overwrite val
            # what is idx into nums of overwrite val? it's m[val][-1]
            self.m[last[0]][last[1]] = self.m[val][-1]

            # val was moved, remove that last idx
            self.m[val].pop()

            # .. empty? don't need it!
            if not self.m[val]:
                del self.m[val]

        return result

    def getRandom(self):
        # just take a random number
        return random.choice(self.nums)[0]
