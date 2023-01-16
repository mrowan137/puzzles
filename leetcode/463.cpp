// Runtime: 187 ms, faster than 40.62% of C++ online submissions for Island Perimeter.
// Memory Usage: 96.2 MB, less than 85.81% of C++ online submissions for Island Perimeter.
class Solution {
 public:
  int islandPerimeter(vector<vector<int>> &grid) {
    const int M = grid.size(), N = grid[0].size();
    int res = 0;

    // 4 for each filled cell, -1 for each neighbor
    for (int i = 0; i < M; ++i) {
      for (int j = 0; j < N; ++j) {
        if (grid[i][j]) {
          int add = 4;
          for (auto c : {pair(i + 1, j), pair(i, j + 1), pair(i - 1, j),
                         pair(i, j - 1)}) {
            if (c.first < 0 || c.first >= M || c.second < 0 || c.second >= N) {
              continue;
            }
            add -= grid[c.first][c.second];
          }
          res += add;
        }
      }
    }

    return res;
  }
};
