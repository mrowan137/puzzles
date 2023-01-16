// Runtime: 15 ms, faster than 41.10% of C++ online submissions for
// Concatenation of Array. Memory Usage: 13 MB, less than 18.92% of C++ online
// submissions for Concatenation of Array.
class Solution {
 public:
  vector<int> getConcatenation(vector<int> &nums) {
    vector<int> res;
    vector<int>::size_type n = nums.size();
    for (vector<int>::size_type i = 0; i < 2 * n; ++i) {
      res.push_back(nums[i % n]);
    }

    return res;
  }
};
