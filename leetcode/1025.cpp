// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Divisor Game.
// Memory Usage: 5.8 MB, less than 90.31% of C++ online submissions for Divisor Game.
//
// 2 --> 1 --> W
// 3 --> 1 --> L
// 4 --> 1,2 --> 2 --> W
// 5 --> 1 --> L
// 6 --> 1,2,3 --> 1 --> W
// 7 --> 1 --> L
// 8 --> 1,2,4 --> W
// 9 --> 1,3 --> L
// Hypothesis:
//   win if n=2*k, lose if n=2*k+1.
//   base case k=1: true by inspection.
//.  now assume true for k = m.
//   want to inductive hypothesis when k = m+1.
//   so win 2*m, lose 2*m+1.
//   now suppose 2*(m+1) = 2*m+2 my start number.
//   clearly I can choose 1 which divides 2*m+2, leaving 2*m+1.
//   but by induction hypothesis it is a losing number.
//   therefore I can choose 1 to force opponent to a losing number.
//.  on the other hand, 2*m+3 is odd number.
//   whatever num divides it is not even, because 3 has no even factors.
//   so odd - odd is an even, which by induction hypothesis is winning number.
//   meaning, no matter what selection is made the opponent get winning number.
class Solution {
 public:
  bool divisorGame(int n) {
    return n%2 == 0;
  }
};
