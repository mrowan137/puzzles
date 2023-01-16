"""
Runtime: 573 ms, faster than 32.87% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.9 MB, less than 63.16% of Python3 online submissions for Find All Duplicates in an Array.

nums are in the range [1,n]
and appearing once or twice
so therefore num-1 is a valid idx

we will create a clever encoding, using quotient math
we have the input num 1 <= x <= n
we define another val y = num times seen
combine those in a way m = f(x, y) to encode info
define that 
  m := (x-1) + y*sz
note that 
  m % sz + 1 = x  [the original number stored at idx]
       m//sz = y  [the num times idx+1 was seen]
which follow because 0<=x-1<sz

so loop through all the nums, 
and record at idx num-1,
how many time it seen
if the num at idx has y=k, 
it means idx was seen k times
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # initialization
        sz = len(nums)
        for i in range(sz):
            nums[i] -= 1

        for i, n in enumerate(nums):
            # decode
            x = n % sz + 1
            y = nums[x - 1] // sz + 1

            # encode
            nums[x - 1] = nums[x - 1] % sz + y * sz

        # write those seen twice to beginning of the array
        write = 0
        for i in range(sz):
            # decode
            y = nums[i] // sz

            # write to front if it's a dup
            if y == 2:
                nums[write] = i + 1
                write += 1

        return nums[:write]
