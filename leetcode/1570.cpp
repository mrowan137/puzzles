// Runtime: 293 ms, faster than 56.61% of C++ online submissions for Dot Product of Two Sparse Vectors.
// Memory Usage: 166.2 MB, less than 85.45% of C++ online submissions for Dot Product of Two Sparse Vectors.
class SparseVector {
 private:
  // nonzero is the list of idx, value
  vector<pair<int, int>> nonzero;

 public:
  SparseVector(vector<int> &nums) {
    // record the idx, val for nonzero values
    for (vector<int>::size_type i = 0; i < nums.size(); ++i) {
      if (nums[i] != 0) {
        nonzero.push_back(pair<int, int>(i, nums[i]));
      }
    }
  }

  // Return the dotProduct of two sparse vectors
  int dotProduct(SparseVector &vec) {
    // iterator for self and vec
    int i = 0, j = 0;

    // accumulate the nonzero multiplications
    int res = 0;

    while (i < nonzero.size() && j < vec.nonzero.size()) {
      // add contribution if first values equal
      if (nonzero[i].first == vec.nonzero[j].first) {
        res += nonzero[i].second * vec.nonzero[j].second;
        ++i;
        ++j;
        continue;
      }

      // push up i and j
      while (i < nonzero.size() and j < vec.nonzero.size() and
             nonzero[i].first < vec.nonzero[j].first) {
        ++i;
      }
      while (i < nonzero.size() and j < vec.nonzero.size() and
             vec.nonzero[j].first < nonzero[i].first) {
        ++j;
      }
    }

    return res;
  }
};
