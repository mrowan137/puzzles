// Runtime: 3 ms, faster than 51.56% of C++ online submissions for Is Subsequence.
// Memory Usage: 6.8 MB, less than 22.11% of C++ online submissions for Is Subsequence.
class Solution {
 public:
  bool isSubsequence(string s, string t) {
    // s is subsequence of t if
    //   1) s[-1] == t[-1] and s[:-1] subseq of t[:-1]
    //   2) s is subseq of t[:-1]
    const int M = s.size(), N = t.size();

    // initialization:
    //   1) bool dp[101][10001] = {};   can pass a list of values, shape implied
    //   2) bool dp[101][10001] = {{}}; can pass brace of braces
    //   3) dynamic
    bool **dp =
        new bool *[M + 1]; // dp is pointer to bool*, and allocated for M+1
    for (int i = 0; i < M + 1; ++i) {
      dp[i] = new bool[N + 1](); // value initialization
    }
    for (int j = 0; j < N + 1; ++j) {
      dp[0][j] = true;
    }

    for (int i = 1; i < M + 1; ++i) {
      for (int j = 1; j < N + 1; ++j) {
        if (s[i - 1] == t[j - 1] and dp[i - 1][j - 1] == true) {
          dp[i][j] = true;
        } else if (dp[i][j - 1] == true) {
          dp[i][j] = true;
        }
      }
    }
    return dp[M][N];
  }
};
