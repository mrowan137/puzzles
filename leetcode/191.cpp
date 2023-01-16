// Runtime: 3 ms, faster than 57.88% of C++ online submissions for Number of 1 Bits.
// Memory Usage: 6 MB, less than 47.68% of C++ online submissions for Number of 1 Bits.
class Solution {
 public:
  int hammingWeight(uint32_t n) {
    // given: 32 bit unsigned integer
    // goal : compute number of 1 bits
    //
    // example: 5 = 101 --> 2
    //
    // observations:
    //   - all hamming weights are between 0 and 32
    //     hw | # of such values
    //     0  | 32 C 0 = 1
    //     1  | 32 C 1 = 32
    //       ...
    //    31  | 32 C 31 = 32
    //    32  | 1
    //
    // implementation:
    //   - masking out the lsb and sum
    //   - write out 32 masks manually and sum
    //   - h(n) = h(n-1) + ???
    //     pattern?
    //     h(111) = 3
    //     h(110) = 2
    //     h(101) = 2
    //     h(100) = 1
    //     h(011) = 2
    //     h(010) = 1
    //     h(001) = 1
    //     h(000) = 0
    //     h(n) = h(n >> 1) & 0xFFFF + lsb
    // go for recursive: O(32) time
    if (n == 0) {
      return 0;
    }
    return (n & 1) + hammingWeight(n >> 1);
  }
};
