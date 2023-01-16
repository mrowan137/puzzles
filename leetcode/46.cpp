// Runtime: 25 ms, faster than 5.03% of C++ online submissions for Permutations.
// Memory Usage: 9.5 MB, less than 5.27% of C++ online submissions for Permutations.
class Solution {
 public:
  vector<vector<int>> permute(vector<int> &nums) {
    set<vector<int>> seen = {};        // track the states we saw so far
    deque<vector<int>> queue = {nums}; // initial state to explore
    while (!queue.empty()) {
      // get state from top of the stack
      vector<int> perm = queue[0];
      queue.pop_front();

      // stash the result and explore it, only if it's a new permutation
      if (seen.find(perm) == seen.end()) {
        // stash
        seen.insert(perm);

        // add other states we want to explore: swap neighbors
        for (int i = 0; i < perm.size() - 1; ++i) {
          swap(perm[i], perm[i + 1]);
          queue.push_back(perm);
          swap(perm[i], perm[i + 1]);
        }
      }
    }

    return vector<vector<int>>(seen.begin(), seen.end());
  }
};
