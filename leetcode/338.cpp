// Runtime: 137 ms, faster than 5.40% of C++ online submissions for Counting Bits.
// Memory Usage: 15.4 MB, less than 22.09% of C++ online submissions for Counting Bits.
//
// Looking for a pattern:
// 1   0001 1
// 2   0010 1
//  3  0011 2
// 4   0100 1
//  5  0101 2
//  6  0110 2
//  7  0111 3
// 8   1000 1
//  9  1001 2
//  10 1010 2
//  11 1011 3
//  12 1100 2
//  13 1101 3
//  14 1110 3
//  15 1111 4
//
// f(12) = f(0b1100) = f(0b110) + f(0b0) = 2 + 0 = 2
//
// strategy: for any given number, the smaller numbers
//           will all be computed, so the results is
//           the num zeros in bitshifted, plut 0b1 & n
// auto IsPowerOfTwo = [](int m) {
//    float log2m = std::log2(m);
//    return std::floor(log2m) == log2m;
//};
class Solution {
 private:
  std::map<int, int> memo_;

  int NumBits(int n) {
    if (memo_.find(n) != memo_.end()) {
      return memo_[n];
    }
    if (n == 0) {
      return 0;
    }
    int res = (n & 1) + NumBits(n >> 1);
    memo_[n] = res;
    return res;
  }

 public:
  vector<int> countBits(int n) {
    vector<int> res = {0};
    for (int i = 1; i < n + 1; ++i) {
      res.push_back(NumBits(i));
    }
    return res;
  }
};
