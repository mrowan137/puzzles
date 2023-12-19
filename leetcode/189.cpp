// Runtime: 19 ms
// Memory Usage: 25.2 MB
class Solution {
 public:
  void rotate(vector<int>& nums, int k) {
    // initialize
    int placed = 0;
    int mod_class = 0;
    int idx = 0;
    int write = nums[idx];
    const int n = nums.size();

    // cycle through elements of each mod class
    while (placed < n) {
      // increment, save, write, and load the next write
      idx += k;
      idx %= n;
      int save = nums[idx];
      nums[idx] = write;
      write = save;

      // value written into correct spot, increment count
      placed += 1;

      // if we loop back to first spot, we shifted all elements
      // in the current mod cycle and can move to the next one
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
