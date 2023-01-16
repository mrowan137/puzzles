// Runtime: 24 ms, faster than 61.03% of C++ online submissions for Majority Element.
// Memory Usage: 19.7 MB, less than 14.26% of C++ online submissions for Majority Element.
class Solution {
 public:
  int majorityElement(vector<int> &nums) {
    std::map<int, int> num_to_count;
    std::set<int> keys;
    for (vector<int>::const_iterator it = nums.begin(); it != nums.end();
         ++it) {
      if (std::find(keys.begin(), keys.end(), *it) != keys.end()) {
        num_to_count[*it] += 1;
      } else {
        num_to_count[*it] = 1;
      }

      keys.insert(*it);
    }

    for (std::map<int, int>::const_iterator pair = num_to_count.begin();
         pair != num_to_count.end(); ++pair) {
      if (pair->second > std::floor(nums.size() / 2)) {
        return pair->first;
      }
    }

    return -1;
  }
};
