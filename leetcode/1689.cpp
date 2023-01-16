// Runtime: 45 ms, faster than 61.89% of C++ online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
// Memory Usage: 13.5 MB, less than 63.77% of C++ online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
class Solution {
 public:
  int minPartitions(string n) {
    int res = INT_MIN;
    for (auto c : n) {
      res = max(res, int(c) - int('0'));
    }
    return res;
  }
};
