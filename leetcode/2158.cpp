// Runtime: 427 ms, faster than 74.98% of C++ online submissions for Amount of New Area Painted Each Day.
// Memory Usage: 131.2 MB, less than 31.31% of C++ online submissions for Amount of New Area Painted Each Day.
class Solution {
 public:
  vector<int> amountPainted(vector<vector<int>> &paint) {
    // 1. find the place to insert the new painted interval
    // 2. merge any overlapping intervals
    vector<int> res;
    map<int, int> painted;
    for (auto &p : paint) {
      //   l                              r
      // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      //   |==============================|   interval to add
      // |===|             |====|      |===|     map
      // curr   |=====|                          map
      //         next
      int l = p[0], r = p[1];
      auto next = painted.upper_bound(l), curr = next;
      if (curr != begin(painted) && prev(curr)->second >= l) {
        curr = prev(next);
        l = curr->second;
      } else {
        curr = painted.insert({l, r}).first;
      }

      // subtract off painted segments
      int new_paint = r - l;
      while (next != end(painted) && next->first < r) {
        new_paint -= min(next->second, r) - next->first;
        r = max(r, next->second);
        painted.erase(next++);
      }
      curr->second = max(r, curr->second);
      res.push_back(max(0, new_paint));
    }
    return res;
  }
};

// TLE
class Solution {
 public:
  vector<int> amountPainted(vector<vector<int>> &paint) {
    int start = INT_MAX;
    int end = INT_MIN;

    for (auto p : paint) {
      start = min(start, p[0]);
      end = max(end, p[1]);
    }

    vector<int> painted(1 + end - start, 0);

    vector<int> worklog;
    for (auto p : paint) {
      int tally = 0;
      for (int i = p[0]; i < p[1]; ++i) {
        tally += (painted[i - start] == 0);
        painted[i - start] = 1;
      }
      worklog.push_back(tally);
    }

    return worklog;
  }
};
