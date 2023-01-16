// Runtime: 6 ms, faster than 57.67% of C++ online submissions for Partition Labels.
// Memory Usage: 6.7 MB, less than 67.98% of C++ online submissions for Partition Labels.
class Solution {
 public:
  vector<int> partitionLabels(string s) {
    map<char, int> char_to_last_idx = {};
    for (int i = 0; i < s.size(); ++i) {
      char_to_last_idx[s[i]] = i;
    }

    // greedy extend the partition as possible
    vector<int> res = {};
    int anchor = 0, hare = 0;
    for (int tortoise = 0; tortoise < s.size(); ++tortoise) {
      hare = max(hare, char_to_last_idx[s[tortoise]]);
      if (tortoise == hare) {
        res.push_back(hare - anchor + 1);
        anchor = tortoise + 1;
      }
    }

    return res;
  }
};

// Runtime: 17 ms, faster than 7.65% of C++ online submissions for Partition Labels.
// Memory Usage: 7.1 MB, less than 10.64% of C++ online submissions for Partition Labels.
class Solution {
 public:
  vector<int> partitionLabels(string s) {
    // given: string
    // goal: largest number of partitions, where letters
    //       in one partition do not appear in any other
    // strategy: make a dict count the occurrence of each letter,
    //           we can add a partition when no letters of type in remaining
    map<char, int> count;
    for (char c : s) {
      count[c] = count.find(c) == count.end() ? 1 : count[c] + 1;
    }

    vector<int> res = {};
    int p = 0;
    unordered_set<char> chars_of_current_partition = {s[0]};
    auto all_keys_have_zero_count = [&](const unordered_set<char> &chars) {
      for (auto c : chars) {
        if (count[c] != 0) {
          return false;
        }
      }
      return true;
    };

    for (char c : s) {
      count[c] -= 1;
      p += 1;
      chars_of_current_partition.insert(c);
      if (all_keys_have_zero_count(chars_of_current_partition)) {
        res.push_back(p);
        p = 0;
        chars_of_current_partition.clear();
      }
    }

    return res;
  }
};
