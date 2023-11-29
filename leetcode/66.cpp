// Runtime: 2 ms
// Memory Usage: 9 MB
class Solution {
 public:
  vector<int> plusOne(vector<int>& digits) {
    int carry = 1;
    for (vector<int>::iterator it = digits.end() - 1;
         it != digits.begin() - 1; --it) {
      *it += carry;
      carry = *it/10;
      *it %= 10;
    }

    if (carry != 0) digits.insert(digits.begin(), carry);
    return digits;
  }
};
