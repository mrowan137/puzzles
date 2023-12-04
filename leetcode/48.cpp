// Runtime: 0 ms
// Memory Usage: 7.4 MB
class Solution {
 public:
  void transpose(vector<vector<int>>& matrix) {
    const int rows = matrix.size(), cols = matrix[0].size();
    for (int i = 0; i < rows; ++i) {
      for (int j = i + 1; j < cols; ++j) {
        std::swap(matrix[i][j], matrix[j][i]);
      }
    }
    return;
  }
  void rotate(vector<vector<int>>& matrix) {
    // note it's the same as transpose and reverse rows
    transpose(matrix);
    for (auto& row : matrix) std::reverse(row.begin(), row.end());
    return;
  }
};
