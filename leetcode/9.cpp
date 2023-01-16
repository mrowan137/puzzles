// Runtime: 42 ms, faster than 8.29% of C++ online submissions for Palindrome Number.
// Memory Usage: 5.8 MB, less than 74.02% of C++ online submissions for Palindrome Number.
class Solution {
 public:
  bool isPalindrome(int x) {
    // early exit
    if (x < 0) {
      return false;
    }

    // construct the number in reverse
    long res = 0;
    int x_copy = x;
    while (x) {
      res += x % 10;
      res *= 10;
      x /= 10;
    }

    return res / 10 == x_copy;
  }
};
