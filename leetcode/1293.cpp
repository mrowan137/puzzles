// Runtime: 19 ms, faster than 87.99% of C++ online submissions for Shortest Path in a Grid with Obstacles Elimination.
// Memory Usage: 10.3 MB, less than 78.44% of C++ online submissions for Shortest Path in a Grid with Obstacles Elimination.
// BFS
class Solution {
 private:
  struct State {
    const int i, j, k;
    State(int i, int j, int k) noexcept : i(i), j(j), k(k) {}

    // required for std::set::insert() and std::set::find()
    bool operator==(const State &rhs) const noexcept {
      return (i == rhs.i && j == rhs.j && k == rhs.k) ? true : false;
    }
  };

  // function object so we can use unordered_set (which needs a hash function)
  struct State_hash {
    size_t operator()(const State &state_to_hash) const noexcept {
      auto h1 = [](const int a, const int b) {
        return 0.5f * (a + b) * (a + b + 1) + b;
      };
      auto h2 = [&h1](const int a, const int b, const int c) {
        return 0.5f * (h1(a, b) + c) * (h1(a, b) + c + 1) + c;
      };

      size_t hash = h2(state_to_hash.i, state_to_hash.j, state_to_hash.k);
      return hash;
    }
  };

 public:
  int shortestPath(vector<vector<int>> &grid, int k) {
    const int m = grid.size(), n = grid[0].size();

    // enough to go around the edges? fast exit!
    if (k >= m + n) {
      return m + n - 2;
    }

    // state has the current location and remaining eliminations (i, j, k)
    State initial_state(0, 0, k);

    // queue stores the (steps_so_far, state)
    deque<pair<int, State>> queue({pair<int, State>(0, initial_state)});

    // keep track of the (steps_so_far, state) we already explored
    unordered_set<State, State_hash> seen = {};

    // while there's states to explore, potentially explore the surrounding
    // cells; 1) the state must be valid, and 2) we must not have seen the state
    // before the first time one reaches the exit, it's the fastest it could
    // have been and we exit;
    while (!queue.empty()) {
      pair<int, State> curr = queue[0];
      queue.pop_front();
      int steps_so_far = curr.first;
      State state = curr.second;

      // exit case -- we reached the end
      if ((state.i == m - 1) && (state.j == n - 1)) {
        return steps_so_far;
      }

      for (pair p : {pair(state.i + 1, state.j), pair(state.i - 1, state.j),
                     pair(state.i, state.j + 1), pair(state.i, state.j - 1)}) {
        const int i = p.first, j = p.second;

        // maybe explore a configuration if in bounds
        if (0 <= i && i < m && 0 <= j && j < n) {
          int new_eliminations = state.k - grid[i][j];
          State new_state(i, j, new_eliminations);

          // new configuration will be explored if it's valid
          if (new_eliminations >= 0 && seen.find(new_state) == seen.end()) {
            seen.insert(new_state);
            queue.push_back(pair<int, State>(steps_so_far + 1, new_state));
          }
        }
      }
    }

    return -1;
  }
};

// DFS -- TLE!
class Solution {
 public:
  int helper(const vector<vector<int>> &grid, const int &i, const int &j,
             const int &c, vector<pair<int, int>> my_path,
             map<tuple<int, int>, int> &memo) {
    const int m = grid.size(), n = grid[0].size();

    // out of bounds? return!
    if (c < 0 || i < 0 || i > m - 1 || j < 0 || j > n - 1) {
      memo[tuple<int, int>(i, j)] = INT_MAX;
      return INT_MAX;
    }

    // crossed our own path before? don't bother!
    if (find(my_path.begin(), my_path.end(), pair<int, int>(i, j)) !=
        my_path.end()) {
      memo[tuple<int, int>(i, j)] = INT_MAX;
      return INT_MAX;
    }

    // at the starting corner? return!
    if (i == 0 && j == 0) {
      memo[tuple<int, int>(i, j)] = grid[0][0] ? (c > 0 ? 0 : INT_MAX) : 0;
      return memo[tuple<int, int>(i, j)];
    }

    my_path.push_back(pair<int, int>(i, j));
    const bool obstacle_c = grid[i][j];
    const int n_steps_so_far =
        min({obstacle_c ? helper(grid, i - 1, j, c - 1, my_path, memo)
                        : helper(grid, i - 1, j, c, my_path, memo),
             obstacle_c ? helper(grid, i + 1, j, c - 1, my_path, memo)
                        : helper(grid, i + 1, j, c, my_path, memo),
             obstacle_c ? helper(grid, i, j - 1, c - 1, my_path, memo)
                        : helper(grid, i, j - 1, c, my_path, memo),
             obstacle_c ? helper(grid, i, j + 1, c - 1, my_path, memo)
                        : helper(grid, i, j + 1, c, my_path, memo)});

    memo[tuple<int, int>(i, j)] =
        n_steps_so_far == INT_MAX ? n_steps_so_far : 1 + n_steps_so_far;
    return memo[tuple<int, int>(i, j)];
  }

  int shortestPath(vector<vector<int>> &grid, int c) {
    const int m = grid.size(), n = grid[0].size();

    // enough to go around the edges? fast exit!
    if (c >= m + n) {
      return m + n - 2;
    }

    // generic case
    vector<pair<int, int>> my_path = {};
    map<tuple<int, int>, int> memo = {};
    int res = helper(grid, m - 1, n - 1, c, my_path, memo);
    return res == INT_MAX ? -1 : res;
  }
};
