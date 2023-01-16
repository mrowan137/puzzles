// Runtime: 55 ms (Beats 65.97%)
// Memory: 12.1 MB (Beats 95.20%)
class Solution {
 public:
  int minDeletionSize(vector<string> &strs) {
    int res = 0;
    for (int j = 0; j < strs[0].size(); ++j) {
      for (int i = 0; i < strs.size() - 1; ++i) {
        if (static_cast<int>(strs[i][j]) > static_cast<int>(strs[i + 1][j])) {
          res += 1;
          break;
        }
      }
    }
    return res;
  }
};
