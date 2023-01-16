// Runtime: 186 ms, faster than 58.75% of C++ online submissions for Random Pick with Blacklist.
// Memory Usage: 73.1 MB, less than 9.66% of C++ online submissions for Random Pick with Blacklist.
//
// given number, and blacklist goal is to pick number not in the blacklist, and
// equal probability of choosing any of those. let N = w + b, where b is length
// of blacklist. consider the first w, [n0, n1, ..., nw]; notice that if m are
// whitelist, n blacklist, then in the remaining [nw+1, nN], there are exactly n
// blacklist nums (to complete the set). so we could make a mapping from
// [0, 1, ..., w] to all the whitelist nums.
class Solution {
 private:
  // number of whitelist nums
  int w;

  // number of blacklit nums
  int b;

  std::set<int> blacklistSet;

  // choose an integer [0, w], get a whitelist num
  std::map<int, int> idxToWhitelistNum;

 public:
  Solution(int n, vector<int> &blacklist) {
    // precompute map from [0, w] to [n0,..., nw]
    b = blacklist.size();
    w = n - b;

    // fast lookup
    blacklistSet = std::set<int>(blacklist.begin(), blacklist.end());

    // initialize a runner to first whitelist
    // num in [nw+1, nN]
    int wRunner = w;
    while (blacklistSet.find(wRunner) != blacklistSet.end()) {
      wRunner += 1;
    }

    for (vector<int>::const_iterator it = blacklist.begin();
         it != blacklist.end(); ++it) {
      if (*it < w) {
        idxToWhitelistNum[*it] = wRunner;
        wRunner += 1;
        while (blacklistSet.find(wRunner) != blacklistSet.end()) {
          wRunner += 1;
        }
      }
    }
  }

  int pick() {
    int r = std::rand() % w;
    return blacklistSet.find(r) == blacklistSet.end() ? r
                                                      : idxToWhitelistNum[r];
  }
};
