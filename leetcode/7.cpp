// Runtime: 0 ms
// Memory Usage: 6.3 MB
class Solution {
 public:
  int reverse(int x) {
    long res = 0;
    while (x != 0) {
      int d = x % 10;
      res *= 10;
      res += d;
      x /= 10;
    }
    if (res > INT_MAX || res < INT_MIN) return 0;
    return static_cast<int>(res);
  }
};
