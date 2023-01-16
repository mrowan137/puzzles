// Runtime: 47 ms, faster than 98.61% of C++ online submissions for Remove All Ones With Row and Column Flips.
// Memory Usage: 26.4 MB, less than 5.82% of C++ online submissions for Remove All Ones With Row and Column Flips.
class Solution {
 public:
  inline bool equivalent(vector<int> x, const vector<int> &y) {
    if (x[0] == y[0]) {
      return x == y;
    } else {
      transform(x.begin(), x.end(), y.begin(), x.begin(), plus<int>());
      return x == vector<int>(x.size(), 1);
    }
  }

  bool removeOnes(vector<vector<int>> &grid) {
    // 2x2
    // possible:
    // 1 1   0 0   1 0   1 1   0 1   0 0   1 0   0 1
    // 1 1   0 0   1 0   0 0   0 1   1 1   0 1   1 0
    //
    // not possible:
    // 1 0   0 1   0 0   0 0
    // 0 0   0 0   0 1   1 0
    //
    // 3x3
    // possible:
    // 0 1 0   1 0 1
    // 1 0 1   0 1 0
    // 0 1 0   1 0 1
    //
    // not possible:
    // 0 0 1   1 1 0   0 0 1   1 1 0   1 0 0
    // 0 1 0   0 1 0   0 1 0   0 1 0   0 0 0
    // 0 0 1   0 1 1   1 0 1   0 1 0   0 0 0
    //
    // conjecture: all rows need to be identical, or exactly opposite

    const vector<int> first_row = grid[0];
    for (vector<vector<int>>::iterator row = grid.begin() + 1;
         row != grid.end(); ++row) {
      if (!equivalent(first_row, *row)) {
        return false;
      }
    }

    return true;
  }
};
