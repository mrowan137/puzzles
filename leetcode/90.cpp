// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Subsets II.
// Memory Usage: 7.5 MB, less than 73.10% of C++ online submissions for Subsets II.
//
// given:
//   - vector of integers
//   - array fits in memory
//
// goal:
//   - compute the 'power set',
//     means the 'set of all possible subsets'
//   - NO DUPLICATE
//
// example:
//   - [1, 2, 2]
//     [ [], [1], [2], [1, 2], [2, 2], [1, 2, 2] ]
//
// ideas:
//   - 'DFS': O(2**N) T, O(2**N) M
//   - 'BFS': O(2**N) T, O(2**N) M
//
// DFS + backtrack
class Solution {
 public:
  void dfs(int i, vector<int> &&curr, vector<vector<int>> &res,
           vector<int> &nums) {
    // assume we are always passed a valid result, so add it
    res.emplace_back(curr);

    // explore others, starting at the first valid element to construct a set
    for (int j = i; j < nums.size(); ++j) {
      // make j to point to the next num different from i, if we are passed ith
      while (j > i && j < nums.size() && nums[j] == nums[j - 1]) {
        ++j;
      }
      if (j >= nums.size()) {
        return;
      }
      curr.emplace_back(nums[j]);
      dfs(j + 1, forward<vector<int>>(curr), res, nums);
      curr.pop_back();
    }
  }

  vector<vector<int>> subsetsWithDup(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res = {};

    // first arg is first elements of nums from which to construct a set
    dfs(0, {}, res, nums);
    return res;
  }
};

// Runtime: 72 ms, faster than 5.34% of C++ online submissions for Subsets II.
// Memory Usage: 9.4 MB, less than 29.78% of C++ online submissions for Subsets II.
// BFS
class Solution {
 public:
  vector<int> nums_;
  vector<vector<int>> powersets_;

  Solution() : powersets_({}) {}

  vector<vector<int>> subsetsWithDup(vector<int> &nums) {
    // initialize with inital state to explore
    sort(nums.begin(), nums.end()); // sort so [1,2] recognized as [2, 1]
    deque<vector<int>> queue = {nums};

    while (!queue.empty()) {
      vector<int> curr = queue[0];
      queue.pop_front();
      if (find(powersets_.begin(), powersets_.end(), curr) ==
          powersets_.end()) {
        powersets_.push_back(curr);

        // visit all subsets we could generate from curr state
        for (int i = 0; i < curr.size(); ++i) {
          // this must initialize nums excluding the current element n
          vector<int> to_explore = curr;
          to_explore.erase(next(to_explore.begin(), i));
          queue.push_back(to_explore);
        }
      }
    }
    // now power_sets_ should be filled with all possible subsets
    return powersets_;
  }
};
