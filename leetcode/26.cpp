// Runtime: 11 ms, faster than 89.61% of C++ online submissions for Remove Duplicates from Sorted Array.
// Memory Usage: 18.4 MB, less than 36.66% of C++ online submissions for Remove Duplicates from Sorted Array.
class Solution {
 public:
  int removeDuplicates(vector<int> &nums) {
    int i = 0;
    for (int j = 0; j < nums.size(); ++j) {
      if (i == 0 || nums[i - 1] != nums[j]) {
        nums[i] = nums[j];
        i += 1;
      }
    }
    return i;
  }
};
