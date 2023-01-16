// Runtime: 7 ms, faster than 90.19% of C++ online submissions for Max Increase to Keep City Skyline.
// Memory Usage: 10 MB, less than 95.76% of C++ online submissions for Max Increase to Keep City Skyline.
// O(N^2)
class Solution {
 public:
  int maxIncreaseKeepingSkyline(vector<vector<int>> &grid) {
    // for each cell, it can grow to min of (max along row, max along col)
    const int m = grid.size();
    const int n = grid[0].size();

    vector<int> row_maxes(m), col_maxes(n);
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        row_maxes[i] = max(row_maxes[i], grid[i][j]);
        col_maxes[j] = max(col_maxes[j], grid[i][j]);
      }
    }

    int res = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j)
        res += min(row_maxes[i], col_maxes[j]) - grid[i][j];
    }

    return res;
  }
};

// Runtime: 23 ms, faster than 12.72% of C++ online submissions for Max Increase to Keep City Skyline.
// Memory Usage: 10.8 MB, less than 6.20% of C++ online submissions for Max Increase to Keep City Skyline.
struct Maxes {
  int u_, r_, d_, l_;
  Maxes()
      : u_(INT_MIN + 1), r_(INT_MIN + 1), d_(INT_MIN + 1), l_(INT_MIN + 1) {}
};

class Solution {
 public:
  int maxIncreaseKeepingSkyline(vector<vector<int>> &grid) {
    const int m = grid.size();
    const int n = grid[0].size();

    // keep track a grid with max to left, right, up, down
    vector<vector<Maxes>> maxes_urdl =
        vector<vector<Maxes>>(m, vector<Maxes>(n, Maxes()));
    for (int i = 0; i < m; ++i) {
      int mx = INT_MIN;
      for (int j = 1; j < n; ++j) {
        mx = max(mx, grid[i][j - 1]);
        maxes_urdl[i][j].r_ = mx;
      }

      mx = INT_MIN;
      for (int j = n - 2; j >= 0; --j) {
        mx = max(mx, grid[i][j + 1]);
        maxes_urdl[i][j].l_ = mx;
      }
    }
    for (int j = 0; j < n; ++j) {
      int mx = INT_MIN;
      for (int i = 1; i < m; ++i) {
        mx = max(mx, grid[i - 1][j]);
        maxes_urdl[i][j].u_ = mx;
      }
      mx = INT_MIN;
      for (int i = m - 2; i >= 0; --i) {
        mx = max(mx, grid[i + 1][j]);
        maxes_urdl[i][j].d_ = mx;
      }
    }
    auto min_along_row_col = [&](const int i, const int j) {
      return min(max(maxes_urdl[i][j].u_, maxes_urdl[i][j].d_),
                 max(maxes_urdl[i][j].l_, maxes_urdl[i][j].r_));
    };

    int res = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        res += std::max(min_along_row_col(i, j) - grid[i][j], 0);
      }
    }

    return res;
  }
};
