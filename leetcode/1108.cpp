// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Defanging an IP Address.
// Memory Usage: 6.1 MB, less than 21.88% of C++ online submissions for Defanging an IP Address.
class Solution {
 public:
  string defangIPaddr(string address) {
    string res = "";
    for (string::iterator it = address.begin(); it != address.end(); ++it) {
      if (*it == '.') {
        res += "[.]";
      } else {
        res += *it;
      }
    }
    return res;
  }
};
