// Runtime: 19 ms
// Memory Usage: 25.2 MB
class Solution {
 public:
  void rotate(vector<int>& nums, int k) {
    int placed = 0;
    int mod_class = 0;
    int idx = 0;
    int write = nums[idx];
    const int n = nums.size();
    while (placed < n) {
      idx += k;
      idx %= n;
      int save = nums[idx];
      nums[idx] = write;
      write = save;
      placed += 1;
      if (idx == mod_class) {
        mod_class += 1;
        idx = mod_class;
        if (idx < n) {
          write = nums[idx];
        }
      }
    }
  }
};
