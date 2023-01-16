// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Count Sorted Vowel Strings.
// Memory Usage: 6.6 MB, less than 9.68% of C++ online submissions for Count Sorted Vowel Strings.
class Solution {
 public:
  vector<int> NumAeiou(int n) {
    // {# ending in a, # ending in e, # ending in i, ...}
    // generate # a     ending per end in a
    // generate # a,e   ending per end in e
    // generate # a,e,i ending per end in i
    // etc.
    //
    // {sum(v[:1]), sum(v[:2]), sum(v[:3]), ...}
    if (n == 1) {
      return vector<int>({1, 1, 1, 1, 1});
    }
    vector<int> num_aeiou = NumAeiou(n - 1);
    vector<int> res;

    for (int i = 0; i < 5; ++i) {
      res.push_back(
          std::accumulate(num_aeiou.begin(), num_aeiou.begin() + i + 1, 0));
    }

    return res;
  }

  int countVowelStrings(int n) {
    vector<int> v = NumAeiou(n);
    return std::accumulate(v.begin(), v.end(), 0);
  }
};
