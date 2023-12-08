// Runtime: 9 ms
// Memory Usage: 7.7 MB
class Solution {
 public:
  bool isPalindrome(string s) {
    // remove non-alphanumeric characters
    string::iterator erase_start = std::remove_if(
      s.begin(),
      s.end(), 
      [](const unsigned char& c){ return !std::isalnum(c); }
    );  // returns iterator to start of 'delete' range 
    s.erase(erase_start, s.end());  // do actual deletion
    std::transform(
      s.begin(), s.end(),  // transform range
      s.begin(),           // start storing transformed
      [](const unsigned char& c){ return std::tolower(c); }
    );
    // check remaining is palindrome
    string::const_iterator l = s.begin(), r = s.end() - 1;
    while (l < r) {
      if (*l != *r) return false;
      ++l;
      --r;
    }
    return true;
  }
};

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
