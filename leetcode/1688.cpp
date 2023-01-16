// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Count of Matches in Tournament.
// Memory Usage: 5.9 MB, less than 69.06% of C++ online submissions for Count of Matches in Tournament.
class Solution {
 public:
  int numberOfMatches(int n) {
    int res = 0;
    while (n) {
      res += n / 2 + (n % 2 == 1);
      n /= 2;
    }
    return res - 1;
  }
};
