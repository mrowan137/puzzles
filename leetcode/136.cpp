// Runtime: 31 ms, faster than 53.23% of C++ online submissions for Single Number.
// Memory Usage: 17 MB, less than 51.79% of C++ online submissions for Single Number.
class Solution {
 public:
  int singleNumber(vector<int> &nums) {
    // use a smart propert of XOR: x^x = 0
    // => only the singleton remain if we xor everything
    // note also 0 ^ T = T, 0 ^ F = F => 0 ^ x = x
    // so 0 can be the initial
    int res = 0;
    for (vector<int>::const_iterator it = nums.begin(); it != nums.end();
         ++it) {
      res ^= *it;
    }
    return res;
  }
};
