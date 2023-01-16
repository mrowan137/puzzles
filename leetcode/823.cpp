// Runtime: 287 ms, faster than 10.36% of C++ online submissions for Binary Trees With Factors.
// Memory Usage: 8.4 MB, less than 98.41% of C++ online submissions for Binary Trees With Factors.
class Solution {
 public:
  static constexpr int kMod_ = 1000000007;
  int numFactoredBinaryTrees(vector<int> &arr) {
    // each x in arr can be a root in a binary tree;
    // let dp[x] be the number of ways to construct the root is x;
    // then for all y, z s.t. y*z = x, dp[x] = sum(dp[y]*dp[z]).
    //
    // algorithm: for each node as a root node, consider all possible
    // pairs of l and r children node, and add the contribution.
    // doing this in increasing order, we can ensure that all nodes
    // less than the current have the correct tally dp[x].
    const int N = arr.size();
    std::sort(arr.begin(), arr.end());
    long *dp = new long[N]();
    for (int i = 0; i < N; ++i) {
      dp[i] = 1;
    }

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < i; ++j) {
        if (arr[i] % arr[j] == 0) { // arr[j] is left child
          auto k = std::find(arr.begin(), arr.end(), arr[i] / arr[j]);
          dp[i] += k != arr.end() ? dp[j] * dp[int(k - arr.begin())] : 0;
          dp[i] %= kMod_;
        }
      }
    }

    return std::accumulate(dp, dp + N, long(0)) % kMod_;
  }
};
