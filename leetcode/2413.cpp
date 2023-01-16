// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Smallest Even Multiple.
// Memory Usage: 5.8 MB, less than 70.77% of C++ online submissions for Smallest Even Multiple.
class Solution {
 public:
  int smallestEvenMultiple(int n) { return n % 2 == 0 ? n : n + n; }
};
