// Runtime: 25 ms
// Memory Usage: 19.8 MB
class Solution {
 public:
  void moveZeroes(vector<int>& nums) {
    vector<int>::iterator write = nums.begin(), read = nums.begin();
    while (read != nums.end()) {
      if (*read != 0) {
        *write = *read;
        ++write;
      }
      read += 1;
    }
    while (write != nums.end()) {
      *write = 0;
      ++write;
    }
    return;
  }
};

