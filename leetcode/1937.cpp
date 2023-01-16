// Runtime: 390 ms, faster than 68.21% of C++ online submissions for Maximum
// Number of Points with Cost. Memory Usage: 129.3 MB, less than 16.58% of C++
// online submissions for Maximum Number of Points with Cost. O(M*N) Use trick
// from the trapping rainwaters Note we take a max over the function
//   max_{k} ( points[i][j] - abs(j - k) + dp[i-1][k] )  , for j >= k
//   points[i][j] - j + max_{k} ( dp[i-1][k] + k )  , for j >= k
// and similar:
//   points[i][j] + j + max_{k} ( dp[i-1][k] - k )  , for j <= k
// this give 2 arrays, the max on the right and on the left, for given j.
// so compute this arrays for each i, and iterate of j using those array.
class Solution {
 public:
  long long maxPoints(vector<vector<int>> &points) {
    const int m = points.size();
    const int n = points[0].size();

    vector<vector<long long>> dp =
        vector<vector<long long>>(m, vector<long long>(n, LONG_MIN));
    for (int k = 0; k < n; ++k) {
      dp[0][k] = points[0][k];
    }

    for (int i = 1; i < m; ++i) {
      vector<long long> dpr(n, LONG_MIN);
      dpr[0] = dp[i - 1][0];
      for (int k = 1; k < n; ++k) {
        dpr[k] = max(dpr[k - 1], dp[i - 1][k] + k);
      }

      vector<long long> dpl(n, LONG_MIN);
      dpl[n - 1] = dp[i - 1][n - 1] - n + 1;
      for (int k = n - 2; k >= 0; --k) {
        dpl[k] = max(dpl[k + 1], dp[i - 1][k] - k);
      }

      for (int j = 0; j < n; ++j) {
        dp[i][j] = max(dpr[j] - j, dpl[j] + j) + points[i][j];
      }
    }
    return *max_element(dp[m - 1].begin(), dp[m - 1].end());
  }
};

// TLE O(M*N*N)
class Solution {
 public:
  long long maxPoints(vector<vector<int>> &points) {
    // dp[i][j] := max point obtained ending at location (i, j)
    //
    // dp[i+1][j] = points[i+1][j] max_{over all j'}( abs(j - j') + dp[i][j'] )
    const int m = points.size();
    const int n = points[0].size();

    vector<vector<long>> dp =
        vector<vector<long>>(m, vector<long>(n, LONG_MIN));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int jp = 0; jp < n; ++jp) {
          if (i == 0) {
            dp[i][j] = points[i][j];
            continue;
          }
          dp[i][j] = max(points[i][j] - abs(j - jp) + dp[i - 1][jp], dp[i][j]);
        }
      }
    }
    return *max_element(dp[m - 1].begin(), dp[m - 1].end());
  }
};
