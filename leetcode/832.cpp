// Runtime: 8 ms, faster than 49.71% of C++ online submissions for Flipping an Image.
// Memory Usage: 8.8 MB, less than 76.23% of C++ online submissions for Flipping an Image.
class Solution {
 public:
  vector<vector<int>> flipAndInvertImage(vector<vector<int>> &image) {
    // givens:
    //   - matrix of 1 and 0
    //   - commutative operations
    //
    // goal:
    //   - flip row horizontally and invert values: v ^= 1 (xor)
    //
    // Example:
    //   - is the two ops actually a single?
    //   orig    horiz     invert
    // 0 0 1 0  0 1 0 0   1 0 1 1
    // 0 1 1 0  0 1 1 0   1 0 0 1
    // 1 0 1 0  0 1 0 1   1 0 1 0
    // 1 0 1 1  1 1 0 1   0 0 1 0
    //
    // approach: for each row, flip it horizontally and toggle

    auto SwapAndInvert = [](vector<int> &row, const int i, const int j) {
      swap(row[i], row[j]);
      row[i] ^= 1;                // 1 becomes 0, 0 becomes 1
      row[j] ^= (i != j) ? 1 : 0; // 1 stays   1, 0 stays   0
    };

    for (auto &row : image) {
      int i = 0;
      int j = row.size() - 1;
      while (i <= j) {
        SwapAndInvert(row, i, j);
        ++i;
        --j;
      }
    }
    return image;
  }
};
