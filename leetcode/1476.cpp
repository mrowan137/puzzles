// Runtime: 53 ms (Beats 24.38%)
// Memory 18 MB (Beats 95.50%)
class SubrectangleQueries {
private:
  vector<vector<int>> &rectangle_;

public:
  SubrectangleQueries(vector<vector<int>> &rectangle) : rectangle_(rectangle) {}

  void updateSubrectangle(int row1, int col1, int row2, int col2,
                          int newValue) {
    for (int i = row1; i < row2 + 1; ++i) {
      for (int j = col1; j < col2 + 1; ++j) {
        rectangle_[i][j] = newValue;
      }
    }
  }

  int getValue(int row, int col) { return rectangle_[row][col]; }
};
