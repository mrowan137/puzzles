// Runtime: 7 ms
// Memory Usage: 15.6 MB
class Solution {
 public:
  string longestCommonPrefix(vector<string>& strs) {
    unsigned int smallest = INT_MAX;
    for (const auto& s : strs) {
      smallest = std::min(smallest, static_cast<unsigned int>(s.size()));
    }

    string res = "";
    size_t i = 0;
    while (i < smallest){
      for (auto s : strs) {
        if (s[i] != strs[0][i]) {
          return res;
        }
      }
      res += strs[0][i++];
    }
    return res;
  }
};
