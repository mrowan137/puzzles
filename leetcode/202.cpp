// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Happy Number.
// Memory Usage: 5.9 MB, less than 62.15% of C++ online submissions for Happy Number.
class Solution {
 public:
  int NextHappyNumber(int x, int n) {
    // push x to the next happy number, n times
    while (n--) {
      int sum_of_squares = 0;
      while (x) {
        sum_of_squares += pow((x % 10), 2);
        x /= 10;
      }
      x = sum_of_squares;
    }

    return x;
  }

  bool isHappy(int n) {
    int x = n, y = n;

    // this will work only because we were told
    // there's a cycle, or it ends in 1
    do {
      x = NextHappyNumber(x, 1);
      y = NextHappyNumber(y, 2);
      if (x == y && x != 1) {
        return false;
      }
    } while (x != y);
    return true;
  }
};
