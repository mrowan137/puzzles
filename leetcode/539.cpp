// Runtime: 95 ms (beats 5.16%)
// Memory: 13.3 MB (beats 98.23%)
class Solution {
 public:
  int findMinDifference(vector<string> &timePoints) {
    // goal: find minimum difference
    // ideas: brute force: O(N^2)
    //        sort them and take min of all the intervals O(N log N)
    auto DecodeTime = [](const string &tp) {
      return 60 * stoi(tp.substr(0, 2)) + stoi(tp.substr(3, 2));
    };

    // Note that % is not modulo in C++ it is division remainder;
    // it satisfied (a/b) + a%b   == a (for b != 0)
    //              -3/2  + -3%2  == -3
    //               -1   +  -2.  == -3
    // To get the traditional 'modulo' you need to
    // ((a%b) + b)%b in case it is negative
    auto mod = [](int a, int b) { return (a % b + b) % b; };

    sort(timePoints.begin(), timePoints.end(),
         [=](const string &tp1, const string &tp2) {
           return DecodeTime(tp1) < DecodeTime(tp2);
         });

    int res = INT_MAX;
    for (int i = 0; i < timePoints.size(); ++i) {
      res = min(res, mod(DecodeTime(timePoints[(i + 1) % timePoints.size()]) -
                             DecodeTime(timePoints[i]),
                         1440));
    }
    return res;
  }
};
