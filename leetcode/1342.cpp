// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Steps to Reduce a Number to Zero.
// Memory Usage: 5.8 MB, less than 95.31% of C++ online submissions for Number of Steps to Reduce a Number to Zero.
class Solution {
 public:
  int numberOfSteps(int num) {
    int res = 0;
    while (num != 0) {
      if (num % 2 == 1) {
        num -= 1;
      } else {
        num /= 2;
      }
      res += 1;
    }
    return res;
  }
};
