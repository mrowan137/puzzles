// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Get Maximum in Generated Array.
// Memory Usage: 5.9 MB, less than 93.03% of C++ online submissions for Get Maximum in Generated Array.
class Solution {
 public:
  int nums_[101];
  Solution() : nums_() {
    // generate the nums
    nums_[1] = 1;
    for (int i = 1; i < 50; ++i) {
      nums_[2 * i] = nums_[i];
      nums_[2 * i + 1] = nums_[i] + nums_[i + 1];
    }

    // stash the cumulative max
    int m = INT_MIN;
    for (int i = 0; i < 101; ++i) {
      m = max(m, nums_[i]);
      nums_[i] = m;
    }
  }

  int getMaximumGenerated(int n) { return nums_[n]; }
};
