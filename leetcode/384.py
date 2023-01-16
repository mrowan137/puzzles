"""
Runtime: 492 ms, faster than 11.51% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.5 MB, less than 39.15% of Python3 online submissions for Shuffle an Array.
"""
# O(N) -- Fisher-Yates algorithm
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums0 = [
            n for n in nums
        ]  # nums0 and nums are different copies of the eras

    def reset(self):
        self.nums = [n for n in self.nums0]
        return self.nums

    def shuffle(self):
        sz = len(self.nums)
        for i in range(sz):
            random_idx = random.choice(range(i, sz))
            self.nums[i], self.nums[random_idx] = (
                self.nums[random_idx],
                self.nums[i],
            )

        return self.nums


"""
Runtime: 301 ms, faster than 76.05% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.6 MB, less than 10.64% of Python3 online submissions for Shuffle an Array.
"""
# Use built in (pseudo) random number generators
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums_orig = nums
        self.nums = [n for n in nums]
        self.N = len(nums)

    def reset(self) -> List[int]:
        return self.nums_orig

    def shuffle(self) -> List[int]:
        for i in range(self.N):
            j = random.choice(range(i, self.N))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums


"""
Runtime: 380 ms, faster than 21.91% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.6 MB, less than 10.64% of Python3 online submissions for Shuffle an Array.
"""
# By hand generation of pseudo random nums
# Complexity ~O(N log(N)) for sorting, ~O(N) for generating random sequence (or worse)
import time


class Solution:
    def __init__(self, nums: List[int]):
        self.nums_orig = nums
        self.nums = [n for n in nums]
        self.N = len(nums)

    def reset(self) -> List[int]:
        return self.nums_orig

    def shuffle(self) -> List[int]:
        # how to define a permutation?
        # 1 2 3 has 6 perms:
        # 123, 132, 213, 231, 312, 321: 3! perms
        # We need to randomly take a state
        # perm can define by a sequence a < b < c, a != b != c
        # i.e. 3 nums with different value
        # We could select digits of clock, if it varies much
        # faster than we are able to sample
        dic = {}
        i = 0
        while i < self.N:
            # pseudo rn is large enough to account for 200 unique nums
            # but this is not ideal because there could be leading 0s,
            # also is the timescale of variation fast enough that
            # the sequence is uncorrelated from one draw to the next?
            pseudo_rand_num = float(str(time.process_time())[-4:])
            if not pseudo_rand_num in dic.values():
                dic[i] = pseudo_rand_num
                i += 1

        num_to_ind = {v: i for i, v in enumerate(self.nums)}
        self.nums = sorted(self.nums, key=lambda i: dic[num_to_ind[i]])

        return self.nums
