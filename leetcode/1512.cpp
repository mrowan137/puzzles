// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Good Pairs.
// Memory Usage: 7.4 MB, less than 15.48% of C++ online submissions for Number of Good Pairs.
class Solution {
 public:
  int numIdenticalPairs(vector<int> &nums) {
    // measure the count
    map<int, int> cnt = {};
    for (auto n : nums) {
      cnt[n] = cnt.find(n) == cnt.end() ? 1 : cnt[n] + 1;
    }

    // for each n in nums; cnt[n] -= 1; res += cnt[n]
    int res = 0;
    for (auto n : nums) {
      res += (--cnt[n]);
    }

    return res;
  }
};
