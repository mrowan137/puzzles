// Runtime: 22 ms, faster than 87.31% of C++ online submissions for Number of Provinces.
// Memory Usage: 14.1 MB, less than 33.56% of C++ online submissions for Number of Provinces.
//
// want to count the number of provinces province, in term of the matrix, is a
// collection of elements a <--> b <--> c, d then abcd is a province.
// so the province is at least 1 (province contains all N),
// and at most N (no one knows anyone but themselves, diag(1))
// Strategy:
//   - maintain a list of the provinces seen.
//   - for each state, explore the tree of known states all the way down,
//     marking ones as seen.
class Solution {
 public:
  void explore(int i, std::set<int> &seen, int N,
               vector<vector<int>> &isConnected) {
    for (int j = 0; j < N; ++j) {
      if (isConnected[i][j] == 1 && seen.find(j) == seen.end()) {
        seen.insert(j);
        explore(j, seen, N, isConnected);
      }
    }
  }

  int findCircleNum(vector<vector<int>> &isConnected) {
    int N = isConnected.size();
    std::set<int> seen;

    int res = 0;
    for (int i = 0; i < N; ++i) {
      if (seen.find(i) == seen.end()) {
        explore(i, seen, N, isConnected);
        res += 1;
      }
    }

    return res;
  }
};
