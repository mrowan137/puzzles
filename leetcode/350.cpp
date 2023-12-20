// Runtime: 3 ms
// Memory Usage: 11.5 MB
/*
  O(n + m) create the count maps.
  Use the unordered_map for O(1) avg lookup time.
  O(min(m, n)) to add intersect elements.
*/
class Solution {
 public:
  vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    // iterate over the shorter
    if (nums1.size() > nums2.size()) return intersect(nums2, nums1);

    // count n1, n2 occurrences
    std::unordered_map<int, int> n1_count, n2_count;
    for (auto n : nums1) n1_count[n] += 1;
    for (auto n : nums2) n2_count[n] += 1;

    // fill the intersection with min count of intersected elements
    vector<int> res = {};
    for (auto pair : n1_count) {
      int count = std::min(n1_count[pair.first], n2_count[pair.first]);
      for (int i = 0; i < count; ++i) res.push_back(pair.first);
    }

    return res;
  }
};
