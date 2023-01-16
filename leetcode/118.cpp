// Runtime: 3 ms, faster than 35.67% of C++ online submissions for Pascal's Triangle.
// Memory Usage: 7.4 MB, less than 33.07% of C++ online submissions for Pascal's Triangle.
class Solution {
 public:
  vector<vector<int>> generate(int num_rows) {
    // base case
    if (num_rows == 1) return vector<vector<int>>({{1}});

    // build up to the current level
    vector<vector<int>> res = generate(num_rows - 1);
    vector<int> last_row;

    // generate the n elements of the nth row
    for (int i = 0; i < num_rows; ++i) {
      int l = (i >= 1) ? res[num_rows - 2][i - 1]: 0;
      int r = (i < (num_rows - 1)) ? res[num_rows - 2][i]: 0;
      last_row.push_back(l + r);
    }

    res.push_back(last_row);
    return res;
  }
};
