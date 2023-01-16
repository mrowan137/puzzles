// Runtime: 4 ms, faster than 55.93% of C++ online submissions for Sqrt(x).
// Memory Usage: 6 MB, less than 25.59% of C++ online submissions for Sqrt(x).
class Solution {
 public:
  int mySqrt(int x) {
    // binary search
    int l = 0, r = x / 2 + 1;
    while (l <= r) {
      long m = (l + r) / 2;
      if (m * m > x) {
        r = m - 1;
      } else if (m * m < x) {
        l = m + 1;
      } else {
        return m;
      }
    }

    return r;
  }
};
