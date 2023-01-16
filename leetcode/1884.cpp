// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Egg Drop With 2 Eggs and N Floors.
// Memory Usage: 6 MB, less than 46.27% of C++ online submissions for Egg Drop With 2 Eggs and N Floors.
#include <cmath>

class Solution {
 public:
  int twoEggDrop(int n) {
    // ideas:
    //   1. drop every floor, requires n drops (but we can do better)
    //   2. it should take the same number of drops to find the breaking
    //      level whether it's at the bottom or the top; so you can afford
    //      to skip a lot of levels going up from the bottom, and less
    //      as you get closer to the top.
    //      suppose m is the optimal number of drops.
    //      if egg breaks first toss, you can identify the breaking level in m -
    //      1 toss,
    //        for a total of (m - 1) + 1 = m toss.
    //      if it didn't break, you have m - 1 toss to find that breaking level,
    //        so if it break on the 2nd toss you must be able to identify in m -
    //        2 toss.
    //      so you may jump m steps at first, then m - 1, then m - 2, ... etc.,
    //      and the number m is the smallest for which sum(m, m-1, m-2, ...) >=
    //      n. but we know those Gauss summ is m*(m+1)/2. so look for the
    //      smallest such number
    // Algebra:
    //   m*(m+1) - 2*n >= 0
    //   m^2 + m - 2*n >= 0
    //   roots = (-1 + sqrt(1 + 8*n))/2
    return std::ceil((std::sqrt(1 + 8 * n) - 1) / 2.0);
  }
};
