// Runtime: 11 ms, faster than 69.42% of C++ online submissions for Shuffle String.
// Memory Usage: 15.3 MB, less than 43.22% of C++ online submissions for Shuffle String.
class Solution {
 public:
  string restoreString(string s, vector<int> &indices) {
    string res(s);
    for (int i = 0; i < s.size(); ++i) {
      res[indices[i]] = s[i];
    }
    return res;
  }
};
