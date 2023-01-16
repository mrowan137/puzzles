// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Convert the Temperature.
// Memory Usage: 6 MB, less than 60.93% of C++ online submissions for Convert the Temperature.
class Solution {
 public:
  vector<double> convertTemperature(double celsius) {
    return {celsius + 273.15, celsius * 1.8 + 32.0};
  }
};
