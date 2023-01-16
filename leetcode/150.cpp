class Solution {
 public:
  int evalRPN(vector<string> &tokens) {
    unordered_map<string, function<int(int, int)>> op = {
        {"+", [](int a, int b) { return a + b; }},
        {"-", [](int a, int b) { return a - b; }},
        {"*", [](int a, int b) { return a * b; }},
        {"/", [](int a, int b) { return a / b; }}};
    deque<int> stack = {};
    for (string &s : tokens) {
      if (op.find(s) == op.end()) {
        stack.push_front(stoi(s));
      } else {
        int b = stack[0];
        stack.pop_front();
        int a = stack[0];
        stack.pop_front();
        stack.push_front(op[s](a, b));
      }
    }

    return stack[0];
  }
};

// TLE
class Solution {
 public:
  int op(const int &a, const int &b, string_view c) {
    if (c[0] == '+') {
      return a + b;
    } else if (c[0] == '-') {
      return a - b;
    } else if (c[0] == '*') {
      return a * b;
    } else if (c[0] == '/') {
      return a / b;
    } else {
      return -1;
    }
  }

  int evalRPN(vector<string> &tokens) {
    vector<string> ops = {"+", "-", "*", "/"};
    while (tokens.size() >= 3) {
      // find a +, -, /, * that preceded by two numbers
      int i = 0;
      while (i < tokens.size()) {
        string a = tokens[i], b = tokens[i + 1], c = tokens[i + 2];
        if ((isdigit(a[0]) && isdigit(b[0]) &&
             find(ops.begin(), ops.end(), c) != ops.end())) {
          int res = op(stoi(a), stoi(b), c);
          tokens.erase(tokens.begin() + i, tokens.begin() + i + 2);
          tokens[i] = to_string(res);
        }
        i += 1;
      }
    }

    return stoi(tokens[0]);
  }
};
