// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Valid Parentheses.
// Memory Usage: 6.2 MB, less than 96.09% of C++ online submissions for Valid Parentheses.
class Solution {
 public:
  bool isValid(string s) {
    // push char onto the stack
    // while closing pair, remove that pair
    vector<char> stack = {};

    auto match = [=](char c) {
      if (c == ')') {
        return '(';
      } else if (c == '}') {
        return '{';
      } else if (c == ']') {
        return '[';
      } else {
        return '@';
      }
    };
    for (char c : s) {
      char curr = c;
      if (!stack.empty() && match(curr) == stack[stack.size() - 1]) {
        stack.pop_back();
        curr = !stack.empty() ? stack[stack.size() - 1] : '@';
      } else {
        stack.push_back(c);
      }
    }

    return stack.size() == 0;
  }
};
