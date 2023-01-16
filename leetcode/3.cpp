// Runtime: 69 ms, faster than 14.87% of C++ online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 8.6 MB, less than 42.65% of C++ online submissions for Longest Substring Without Repeating Characters.
class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    // given:
    //   string
    //
    // find:
    //   longest substring without repeating characters;
    //   substring is any contiguous subset of letters;
    //
    // approaches:
    //   1. recursion considering 3 cases : s[0:-1], s[1:], s[1:-1]
    //   2. dynamic programming: compute longest substring
    //      terminating at given idx: dp[i] represent longest
    //      string without repeating char ending at idx i
    //   3. dragging pointer: start on the left, lengthen range
    //      as long as all the letters are unqique; start a new
    //      measurement if we saw a unique letter; any cell can be
    //      the starting cell of the longest substring
    int i = 0;
    int res = 0;
    map<char, int> char_to_count = {};
    for (int j = 0; j < s.size(); ++j) {
      if (char_to_count.find(s[j]) == char_to_count.end() ||
          char_to_count[s[j]] == 0) {
        char_to_count[s[j]] = 1;
      } else {
        char_to_count[s[j]] += 1;
        auto all_unique = [&](const map<char, int> &char_to_count) {
          int m = INT_MIN;
          for (auto x : char_to_count) {
            m = max(m, x.second);
          }

          return m <= 1;
        };
        while (!all_unique(char_to_count)) {
          char_to_count[s[i]] -= 1;
          i += 1;
        }
      }

      res = max(res, j - i + 1);
    }

    return res;
  }
};
