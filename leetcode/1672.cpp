// Runtime: 4 ms, faster than 84.18% of C++ online submissions for Richest Customer Wealth.
// Memory Usage: 8.2 MB, less than 9.24% of C++ online submissions for Richest Customer Wealth.
class Solution {
 public:
  int maximumWealth(vector<vector<int>> &accounts) {
    int res = INT_MIN;
    for (auto account : accounts) {
      res = std::max(res, std::accumulate(account.begin(), account.end(), 0));
    }

    return res;
  }
};
