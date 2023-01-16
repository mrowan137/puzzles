// Runtime: 4 ms, faster than 56.58% of C++ online submissions for Check if the
// Sentence Is Pangram. Memory Usage: 6.5 MB, less than 47.17% of C++ online
// submissions for Check if the Sentence Is Pangram.

#include <numeric>

class Solution {
 public:
  int letterToIdx(char x) { return static_cast<int>(x) - 97; }

  bool checkIfPangram(string sentence) {
    int seen[26] = {0};
    for (string::const_iterator it = sentence.begin(); it != sentence.end();
         ++it) {
      seen[letterToIdx(*it)] = 1;
      int sum = 0;
      if (std::accumulate(seen, seen + 26, sum) == 26) {
        return true;
      }
    }

    return false;
  }
};
