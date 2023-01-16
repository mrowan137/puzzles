// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Power of Four.
// Memory Usage: 5.9 MB, less than 72.38% of C++ online submissions for Power of Four.
class Solution {
 public:
  bool isPowerOfFour(int n) {
    if (n < 1) {
      return false;
    }
    // a power of 4 is a power of 2
    // but not an 'odd' power of 2
    // we can mask out to check it's a sum of powers of four:
    //    0101010101 && n    == 0101010101
    // and check also it's a power of two (e.g. for n = 4):
    //    n ?= 0000100
    //   ~n  = 1111011 --> iff it's a power of two, to the left of
    //                     rightmost bits becomes 1s (including the significant
    //                     bit), and the right is all 1s
    //  n-1  = 0000011 --> to the right of significant bit becomes all 1s iff 2
    //  power
    bool isSumOfPowersOfFour = (0x55555555 | n) == 0x55555555;
    bool isPowerOfTwo = (~n & (n - 1)) == n - 1;

    return isSumOfPowersOfFour && isPowerOfTwo;
  }
};
