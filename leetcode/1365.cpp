// Runtime: 18 ms, faster than 60.97% of C++ online submissions for How Many Numbers Are Smaller Than the Current Number.
// Memory Usage: 11 MB, less than 7.31% of C++ online submissions for How Many Numbers Are Smaller Than the Current Number.
class Solution {
 public:
  std::vector<int> smallerNumbersThanCurrent(std::vector<int> nums) {
    std::vector<int> nums_copy = nums;
    std::sort(nums_copy.begin(), nums_copy.end());
    std::set<int> seen;
    std::map<int, int> num_to_idx;

    for (int i = 0; i < nums_copy.size(); ++i) {
      if (std::find(seen.begin(), seen.end(), nums_copy[i]) == seen.end()) {
        // since nums_copy is sorted, this is the
        // count of nums that are smaller than n
        num_to_idx[nums_copy[i]] = i;
        seen.insert(nums_copy[i]);
      }
    }

    vector<int> res;
    for (auto n : nums) {
      res.push_back(num_to_idx[n]);
    }

    return res;
  }
};
