// Runtime: 4 ms, faster than 94.96% of C++ online submissions for Final Value of Variable After Performing Operations.
// Memory Usage: 14.1 MB, less than 58.47% of C++ online submissions for Final Value of Variable After Performing Operations.
class Solution {
 public:
  int finalValueAfterOperations(vector<string> &operations) {
    auto Op = [](std::string op, int &n) {
      if (op == "--X" || op == "X--") {
        n -= 1;
      } else if (op == "X++" || op == "++X") {
        n += 1;
      }
    };

    int res = 0;
    for (vector<string>::const_iterator it = operations.begin();
         it != operations.end(); ++it) {
      Op(*it, res);
    }

    return res;
  }
};
