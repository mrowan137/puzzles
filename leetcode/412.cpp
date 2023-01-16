// Runtime: 21 ms, faster than 5.23% of C++ online submissions for Fizz Buzz.
// Memory Usage: 10.1 MB, less than 34.21% of C++ online submissions for Fizz Buzz.
// O(N) time, O(1) memory
class Solution {
 public:
  vector<string> fizzbuzz_;
  Solution() : fizzbuzz_(vector<string>(1e4, " ")) {
    for (int i = 1; i <= 1e4; ++i) {
      string ans = (i % 3 == 0 || i % 5 == 0) ? "" : to_string(i);
      if (i % 3 == 0) {
        ans = "Fizz";
      }
      if (i % 5 == 0) {
        ans += "Buzz";
      }
      fizzbuzz_[i - 1] = ans;
    }
  }

  vector<string> fizzBuzz(int n) {
    return vector<string>(fizzbuzz_.begin(), fizzbuzz_.begin() + n);
  }
};
