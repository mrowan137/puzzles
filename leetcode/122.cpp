// Runtime: 5 ms
// Memory Usage: 13.3 MB
class Solution {
 public:
  int maxProfit(vector<int>& prices) {
    int profit = 0;

    // look into the future, accumulate profits
    for (size_t i = 0; i < prices.size() - 1; ++i) {
      profit += ( (prices[i+1] - prices[i])
                  *static_cast<int>(prices[i+1] - prices[i] > 0) );
    }

    return profit;
  }
};
