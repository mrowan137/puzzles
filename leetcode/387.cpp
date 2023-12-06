// Runtime: 31 ms
// Memory Usage: 11.1 MB
class Solution {
 public:
  int firstUniqChar(string s) {
    std::unordered_map<char, int> count;
    for (const auto& c : s) {
      count[c] += 1;
    }
    for (size_t i = 0; i < s.size(); ++i) {
      if (count[s[i]] == 1) return i;
    }
    return -1;
  }
};
