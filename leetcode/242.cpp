// Runtime: 10 ms
// Memory Usage: 7.8 MB
class Solution {
 public:
  bool isAnagram(string s, string t) {
    std::unordered_map<char, int> count;
    for (const auto& c : s) count[c] += 1;
    for (const auto& c : t) count[c] -= 1;
    for (const auto& pair : count) {
      if (pair.second != 0) return false;
    }
    return true;
  }
};
