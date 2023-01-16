// Runtime: 437 ms, faster than 15.15% of C++ online submissions for Remove All Adjacent Duplicates In String.
// Memory Usage: 9.9 MB, less than 95.61% of C++ online submissions for Remove All Adjacent Duplicates In String.
class Solution {
 public:
  string removeDuplicates(string s) {
    string::iterator it = s.begin();
    while (s != "" && it != s.end()-1) {
      if (*it == *(it+1)) {
        s.erase(it, it+2);
        it = max(s.begin(), it - 1);
      } else {
        it += 1;
      }
    }
    return s;
  }
};
