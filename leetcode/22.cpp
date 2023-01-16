// Runtime: 25 ms, faster than 7.79% of C++ online submissions for Generate Parentheses.
// Memory Usage: 13.7 MB, less than 57.89% of C++ online submissions for Generate Parentheses.
class Solution {
 public:
  vector<string> generateParenthesis(int n) {
    if (n == 0) {
      return vector<string>({""});
    }

    vector<string> res;
    for (int i = 1; i <= int(n / 2); ++i) {
      vector<string> l = generateParenthesis(i);
      vector<string> r = generateParenthesis(n - i);
      for (auto sl : l) {
        for (auto sr : r) {
          if (std::find(res.begin(), res.end(), sl + sr) == std::end(res)) {
            res.push_back(sl + sr);
          }
          if (std::find(res.begin(), res.end(), sr + sl) == std::end(res)) {
            res.push_back(sr + sl);
          }
        }
      }
    }
    for (auto s : generateParenthesis(n - 1)) {
      res.push_back("(" + s + ")");
    }

    return res;
  }
};
