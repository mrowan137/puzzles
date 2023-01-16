// Runtime: 410 ms, faster than 7.48% of C++ online submissions for Minimize
// Product Sum of Two Arrays. Memory Usage: 105.5 MB, less than 93.73% of C++
// online submissions for Minimize Product Sum of Two Arrays.
class Solution {
 public:
  int minProductSum(vector<int> &nums1, vector<int> &nums2) {
    std::sort(nums1.begin(), nums1.end());
    std::sort(nums2.begin(), nums2.end());
    int res = 0;
    vector<int>::const_iterator it2 = nums2.end() - 1;
    for (vector<int>::const_iterator it1 = nums1.begin(); it1 != nums1.end();
         ++it1) {
      res += (*it1) * (*it2);
      it2 -= 1;
    }

    return res;
  }
};
