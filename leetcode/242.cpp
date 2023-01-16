// Runtime: 20 ms, faster than 30.75% of C++ online submissions for Valid Anagram.
// Memory Usage: 7.3 MB, less than 45.46% of C++ online submissions for Valid Anagram.
class Solution {
 public:
  bool isAnagram(string s, string t) {
    // early exit
    if (s.size() != t.size()) {
      return false;
    }

    // counts shall be the same
    map<char, int> counts = {};
    for (char c : s) {
      counts[c] = (counts.find(c) == counts.end() ? 1 : counts[c] + 1);
    }
    for (char c : t) {
      counts[c] -= 1;
    }

    // now all the keys should be 0
    using pair_type = decltype(counts)::value_type;
    auto max_pair = max_element(counts.begin(), counts.end(),
                                [](const pair_type &a, const pair_type &b) {
                                  return a.second < b.second;
                                });
    auto min_pair = min_element(counts.begin(), counts.end(),
                                [](const pair_type &a, const pair_type &b) {
                                  return a.second < b.second;
                                });
    return max_pair->second == 0 && min_pair->second == 0;
  }
};
