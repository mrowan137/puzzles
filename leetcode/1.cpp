// Runtime: 9 ms
// Memory Usage: 12.7 MB
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    // record map of (needed := target - x) --> (index of x)
    // then search nums for needed; when you find it, the indices
    // are the indices of `needed` you just found, and index of `x`
    // stored before, which satisfies `needed` + `x` == `target`
    std::unordered_map<int, int> needed_to_residual_idx;
    for (size_t i = 0; i < nums.size(); ++i) {
      needed_to_residual_idx[target - nums[i]] = i;
    }

    for (size_t i = 0; i < nums.size(); ++i) {
      if (needed_to_residual_idx.find(nums[i]) != needed_to_residual_idx.end()
          && needed_to_residual_idx[nums[i]] != i) {
        return {static_cast<int>(i), needed_to_residual_idx[nums[i]]};
      }
    }

    return {-1, -1};
  }
};
