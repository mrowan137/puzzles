// Runtime: 209 ms, faster than 65.38% of C++ online submissions for Maximum Split of Positive Even Integers.
// Memory Usage: 40.6 MB, less than 47.35% of C++ online submissions for Maximum Split of Positive Even Integers.
// big brain O(N)
class Solution {
 public:
  vector<long long> maximumEvenSplit(long long finalSum) {
    if (finalSum % 2) {
      return {};
    }

    // we just want the longest one, build it from the smallest nums we can
    vector<long long> res = {};
    long long cur = 0;
    long long i = 2;
    // 2, 4, 6, ...,
    // target= 14
    //      2, 4, 6,
    // cur  2, 6, 12
    while (cur + i <= finalSum) {
      res.push_back(i);
      cur += i;
      i += 2;
    }

    // now we have everything but the last sum, which is wrong
    // and it must be modified
    *prev(res.end()) += finalSum - cur;

    return res;
  }
};

// TLE
class Solution {
 public:
  void dfs(vector<long long> &sequence, long long target,
           vector<vector<long long>> &res) {
    if (target == 0) {
      res.push_back(sequence);
      return;
    }
    for (long long i = (sequence.size() > 0 ? *prev(sequence.end()) : 0) + 2;
         i <= target; i += 2) {
      sequence.push_back(i);
      dfs(sequence, target - i, res);
      sequence.pop_back();
    }
    return;
  }

  vector<long long> maximumEvenSplit(long long finalSum) {
    // goal: split sum into unique integers
    // idea: DFS to generate all possible sums of unqique integers --> return
    // longest sequence
    vector<long long> sequence = {};
    vector<vector<long long>> res = {};
    dfs(sequence, finalSum, res);
    auto ret = max_element(res.begin(), res.end(), [](auto v1, auto v2) {
      return v1.size() < v2.size();
    });
    return res.size() == 0 ? vector<long long>() : *ret;
  }
};
