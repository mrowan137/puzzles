// Runtime: 16 ms
// Memory Usage: 17.2 MB

/*
  O(n) iterate through array.
*/
class Solution {
 public:
  int singleNumber(vector<int>& nums) {
    // use a sneaky property of XOR:
    // a XOR a XOR b = b
    int res = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
      res ^= nums[i];
    }

    return res;
  }
};
