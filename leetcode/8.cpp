// Runtime: 4 ms
// Memory Usage: 7.7 MB
class Solution {
 public:
  std::map<char, int> c_to_d = {
    {'0' , 0}, {'1' , 1}, {'2' , 2}, {'3' , 3}, {'4' , 4},
    {'5' , 5}, {'6' , 6}, {'7' , 7}, {'8' , 8}, {'9' , 9}
  };
  int myAtoi(string s) {
    // remove leading whitespace
    string::const_iterator erase_end = s.begin();
    while (*erase_end == ' ') ++erase_end;
    s.erase(s.begin(), erase_end);

    // read sign
    int sign = s[0] == '-' ? -1 : 1;

    // convert rest
    long long rest = 0;
    for (auto it = s.begin() + (s[0] == '-' || s[0] == '+' ? 1 : 0); 
         it != s.end(); ++it) {
      if (!std::isdigit(*it)) break;
      rest *= 10;
      rest += c_to_d[*it];
      if (rest > INT_MAX) break;
    }
    rest *= sign;
    rest = (rest > INT_MAX ? INT_MAX : rest);
    rest = (rest < INT_MIN ? INT_MIN : rest);
    return rest;
  }
};
