// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Climbing Stairs.
// Memory Usage: 6.1 MB, less than 30.29% of C++ online submissions for Climbing Stairs.
class Solution {
 private:
  std::map<int, int> memo;

 public:
  int climbStairs(int n) {
    if (memo.find(n) != memo.end()) {
      return memo[n];
    }
    if (n == 0 or n == 1) {
      return 1;
    }
    memo[n] = climbStairs(n - 1) + climbStairs(n - 2);
    return memo[n];
  }
};
