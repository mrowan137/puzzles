// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Jewels and Stones.
// Memory Usage: 6.1 MB, less than 96.01% of C++ online submissions for Jewels and Stones.
#include <string>

class Solution {
 public:
  int numJewelsInStones(string jewels, string stones) {
    int numJewels = 0;
    for (string::const_iterator it = stones.begin(); it != stones.end(); ++it) {
      if (jewels.find(*it) != std::string::npos) {
        numJewels += 1;
      }
    }

    return numJewels;
  }
};
