// Runtime: 101 ms
// Memory Usage: 72 MB

/*
  O(n) to fill the counter and search.
*/
#include <map>

class Solution {
 public:
  bool containsDuplicate(vector<int>& nums) {
    // count occurrences
    std::unordered_map<int, int> counter;
    for (size_t i = 0; i < nums.size(); ++i) {
      counter[nums[i]] += 1;
    }

    // check for duplicates
    for (auto pair : counter) {
      if (pair.second > 1) {
        return true;
      }
    }

    return false;
  }
};
