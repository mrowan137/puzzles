// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Maximum Nesting Depth of the Parentheses.
// Memory Usage: 6.2 MB, less than 84.71% of C++ online submissions for Maximum Nesting Depth of the Parentheses.
class Solution {
 public:
  int maxDepth(string s) {
    int stack_size = 0;
    int max_stack_size = 0;
    for (string::const_iterator it = s.begin(); it != s.end(); ++it) {
      if (*it == '(') {
        stack_size += 1;
      } else if (*it == ')') {
        stack_size -= 1;
      }
      max_stack_size = max(max_stack_size, stack_size);
    }

    return max_stack_size;
  }
};
