// lot's of ways to reverse a vector in C++!
// std::reverse:
//   Runtime: 36 ms, faster than 87.20% of C++ online submissions for
//   Squares of a Sorted Array. Memory Usage: 26.7 MB, less than 31.02% of
//   C++ online submissions for Squares of a Sorted Array.
//   reverse(res.begin(), res.end());
//   return res;
//
// reverse iterators:
//   Runtime: 37 ms, faster than 85.19% of C++ online submissions for
//   Squares of a Sorted Array. Memory Usage: 27.5 MB, less than 5.16% of
//   C++ online submissions for Squares of a Sorted Array. return
//   vector<int>(res.rbegin(), res.rend());
//
// swap:
//   Runtime: 36 ms, faster than 87.20% of C++ online submissions for
//   Squares of a Sorted Array. Memory Usage: 26.9 MB, less than 26.04% of
//   C++ online submissions for Squares of a Sorted Array. for (auto left =
//   res.begin(), right = prev(res.end()); left < right; ++left, --right)
//   swap(*left, *right); return res;
//
// transform:
//   Runtime: 37 ms, faster than 85.19% of C++ online submissions for
//   Squares of a Sorted Array. Memory Usage: 26.9 MB, less than 16.14% of
//   C++ online submissions for Squares of a Sorted Array.
class Solution {
 public:
  vector<int> sortedSquares(vector<int> &nums) {
    vector<int> res = {};
    vector<int>::const_iterator left = nums.begin(), right = nums.end() - 1;
    while (left <= right) {
      if ((*left) * (*left) > (*right) * (*right)) {
        res.push_back((*left) * (*left));
        ++left;
      } else {
        res.push_back((*right) * (*right));
        --right;
      }
    }

    transform(res.begin(), res.begin() + res.size() / 2, res.rbegin(),
              res.begin(), [](int &x, int &y) {
                swap(x, y);
                return x;
              });
    return res;
  }
};
