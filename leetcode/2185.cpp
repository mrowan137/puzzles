// Runtime: 16 ms, faster than 54.58% of C++ online submissions for Counting Words With a Given Prefix.
// Memory Usage: 9.9 MB, less than 74.25% of C++ online submissions for Counting Words With a Given Prefix.
class Solution {
 public:
  int prefixCount(vector<string> &words, string pref) {
    int res = 0;
    for (const string_view &w : words) {
      res += w.find(pref) == 0;
    }
    return res;
  }
};
