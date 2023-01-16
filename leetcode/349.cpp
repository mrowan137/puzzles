// Runtime: 7 ms, faster than 70.18% of C++ online submissions for Intersection of Two Arrays.
// Memory Usage: 10.5 MB, less than 29.96% of C++ online submissions for Intersection of Two Arrays.
class Solution {
 public:
  vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
    vector<int> res;
    unordered_set<int> m(nums1.begin(), nums1.end());
    for (vector<int>::iterator it = nums2.begin(); it != nums2.end(); ++it) {
      if (m.count(*it)) {
        res.push_back(*it);
        m.erase(*it);
      }
    }

    return res;
  }
};
