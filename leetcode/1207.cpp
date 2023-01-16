// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Unique Number of Occurrences.
// Memory Usage: 8.1 MB, less than 53.59% of C++ online submissions for Unique Number of Occurrences.
class Solution {
 public:
  bool uniqueOccurrences(vector<int>& arr) {
    // generate the counts
    map<int, int> count;
    for (auto x : arr) {
      count[x] = count.find(x) == count.end() ? 1 : count[x] + 1;
    }

    // count the counts
    map<int, int> count_of_count;
    for (auto p : count) {
      if (count_of_count.find(count[p.first]) != count_of_count.end()) {
        return false;
      }
      count_of_count[count[p.first]] = 1;
    }
    return true;
  }
};
