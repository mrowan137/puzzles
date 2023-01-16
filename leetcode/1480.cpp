// Runtime: 3 ms, faster than 76.26% of C++ online submissions for Running Sum of 1d Array.
// Memory Usage: 8.6 MB, less than 38.38% of C++ online submissions for Running Sum of 1d Array.
class Solution {
 public:
  vector<int> runningSum(vector<int>& nums) {
    vector<int> res;
    res.push_back(0);
    for (auto n : nums) {
      res.push_back(n + *(res.end() - 1));
    }
    res.erase(res.begin());
    return res;
  }
};
