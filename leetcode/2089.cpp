// Runtime: 7 ms, faster than 63.20% of C++ online submissions for Find Target Indices After Sorting Array.
// Memory Usage: 11.7 MB, less than 60.41% of C++ online submissions for Find Target Indices After Sorting Array.
class Solution {
 public:
  vector<int> targetIndices(vector<int> &nums, int target) {
    vector<int> res;

    for (vector<int>::size_type i = 0; i != nums.size(); ++i) {
      for (vector<int>::size_type j = i + 1; j != nums.size(); ++j) {
        if (nums[j] < nums[i]) {
          int tmp = nums[i];
          nums[i] = std::move(nums[j]);
          nums[j] = tmp;
        }
      }
      if (nums[i] == target) {
        res.push_back(i);
      }
    }
    return res;
  }
};
