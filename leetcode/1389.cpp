// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Create Target Array in the Given Order.
// Memory Usage: 8.5 MB, less than 10.42% of C++ online submissions for Create Target Array in the Given Order.
class Solution {
 public:
  vector<int> createTargetArray(vector<int> &nums, vector<int> &index) {
    vector<int> res = {};
    for (int i = 0; i < nums.size(); ++i) {
      res.insert(res.begin() + index[i], nums[i]);
    }

    return res;
  }
};
