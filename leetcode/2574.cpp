// Runtime: 7 ms (Beats 81.40%)
// Memory: 11.3 MB (Beats 27.74%)
class Solution {
 public:
  vector<int> leftRigthDifference(vector<int> &nums) {
    vector<int> left = vector<int>(nums.size());
    std::partial_sum(nums.begin(), nums.end() - 1, std::next(left.begin()));

    vector<int> right = vector<int>(nums.size());
    std::partial_sum(nums.rbegin(), nums.rend() - 1, std::next(right.rbegin()));

    vector<int> res = vector<int>(nums.size());
    for (int i = 0; i < res.size(); ++i) {
      res[i] = left[i] > right[i] ? left[i] - right[i] : right[i] - left[i];
    }

    return res;
  }
};
