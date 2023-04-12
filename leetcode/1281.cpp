// Runtime: 0 ms (Beats 100%)
// Memory: 6 MB (Beats 6.7%)
class Solution {
 public:
  int subtractProductAndSum(int n) {
    int digits_sum = 0, digits_product = 1;
    while (n) {
      digits_sum += n % 10;
      digits_product *= n % 10;
      n /= 10;
    }
    return digits_product - digits_sum;
  }
};
