// Runtime: 2 ms, faster than 44.26% of C++ online submissions for Remove Vowels from a String.
// Memory Usage: 6.3 MB, less than 77.87% of C++ online submissions for Remove Vowels from a String.
class Solution {
 public:
  string removeVowels(string s) {
    string res = "";
    string vowels = "aeiou";
    for (auto c : s) {
      if (vowels.find(c) == string::npos) res.append(1, c);
    }

    return res;
  }
};
