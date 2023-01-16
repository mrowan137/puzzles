// Runtime: 14 ms, faster than 78.69% of C++ online submissions for Trapping Rain Water.
// Memory Usage: 21 MB, less than 5.64% of C++ online submissions for Trapping Rain Water.
class Solution {
 public:
  int trap(vector<int> &height) {
    const int N = height.size();
    int *l = new int[N](), *r = new int[N]();
    l[N - 1] = height[N - 1];
    r[0] = height[0];
    for (int i = 1; i < N; ++i) {
      int j = N - 1 - i;
      l[j] = std::max(height[j], l[j + 1]);
      r[i] = std::max(height[i], r[i - 1]);
    }

    int *res = new int[N]();
    for (int i = 0; i < N; ++i) {
      res[i] = std::max(std::min(r[i], l[i]) - height[i], 0);
    }
    return std::accumulate(res, res + N, 0);
  }
};
