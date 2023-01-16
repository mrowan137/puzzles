// Runtime: 0 ms (Beats 100%)
// Memory: 6.5 MB (Beats 24.48%)
class Solution {
 public:
  bool allUpper(const string &word) {
    // return true if all upper
    if (word.empty()) {
      return true;
    }
    return (isupper(word[0]) && allUpper(word.substr(1, word.size() - 1)));
  }

  bool allLower(const string &word) {
    // return true if all lower
    // return true if all upper
    if (word.empty()) {
      return true;
    }
    return (islower(word[0]) && allLower(word.substr(1, word.size() - 1)));
  }
  bool detectCapitalUse(string word) {
    // word should be all upper, all lower, or first upper
    // in otherwords, there are 3 cases:
    //   - all upper
    //   - first upper, rest lower
    //   - first lower, rest lower

    // empty string
    if (word.empty()) {
      return true;
    }

    const string &rest = word.substr(1, word.size() - 1);
    return allLower(rest) || allUpper(word) ? true : false;
  }
};
