// Runtime: 6 ms, faster than 69.22% of C++ online submissions for Valid Palindrome.
// Memory Usage: 7.4 MB, less than 51.53% of C++ online submissions for Valid Palindrome.
#include <cctype>

class Solution {
 public:
  bool isPalindrome(string s) {
    string::const_iterator l = s.begin(), r = (s.end()-1);
    while (l < r) {
      if (!std::isalnum(*l)) {++l; continue;}
      if (!std::isalnum(*r)) {--r; continue;}
      if (std::tolower(*l) != std::tolower(*r)) {return false;}
      ++l;
      --r;
    }
    return true;
  }
};
