// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Kids With the Greatest Number of Candies.
// Memory Usage: 8.9 MB, less than 58.99% of C++ online submissions for Kids With the Greatest Number of Candies.
class Solution {
 public:
  vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies) {
    auto m = max_element(candies.begin(), candies.end());
    vector<bool> res = {};
    for (auto c : candies) {
      res.push_back(c + extraCandies >= *m ? true : false);
    }
    return res;
  }
};
