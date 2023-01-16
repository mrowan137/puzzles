// Runtime: 13 ms (beats 47.60%)
// Memory: 8.1 MB (beats 89.2%)
class Solution {
 public:
  int countBattleships(vector<vector<char>> &board) {
    const int m = board.size(), n = board[0].size();

    // count battleships going in each direction
    // note it's only 1 x k or k x 1 dimensions,
    // and separated by at least a space in the
    // perpendicular direction, therefore if we
    // hit a ship in the parallel direction and
    // there's nothing next to hit, we can be sure
    // of the alignment
    int res = 0;

    // horizontal direction
    bool on_a_battleship = false;
    for (int i = 0; i < m; ++i) {
      res += static_cast<int>(on_a_battleship); // might have been on battleship
      on_a_battleship = false;                  // at end of previous column
      for (int j = 0; j < n; ++j) {
        bool nothing_above = (i - 1 >= 0) ? (board[i - 1][j] == '.') : true;
        bool nothing_below = (i + 1 < m) ? (board[i + 1][j] == '.') : true;
        bool vertically_aligned = nothing_above && nothing_below;

        if (board[i][j] == '.') {
          if (on_a_battleship == true) { // got off battleship
            on_a_battleship = false;
            res += 1;
          } else { // still not on a battleship
            continue;
          }
        } else if (board[i][j] == 'X') {
          if (vertically_aligned) {
            if (on_a_battleship == true) { // still on a battleship
              continue;
            } else { // got on a battleship
              on_a_battleship = true;
            }
          } else { // hit a vertically aligned ship
            continue;
          }
        }
      }
    }
    res += static_cast<int>(on_a_battleship); // tally if still on the last ship

    // vertical direction
    on_a_battleship = false;
    for (int j = 0; j < n; ++j) {
      res += static_cast<int>(on_a_battleship); // might have been on battleship
      on_a_battleship = false;                  // at end of previous column
      for (int i = 0; i < m; ++i) {
        bool nothing_left = (j - 1 >= 0) ? (board[i][j - 1] == '.') : true;
        bool nothing_right = (j + 1 < n) ? (board[i][j + 1] == '.') : true;
        bool horizontally_aligned = nothing_left && nothing_right;

        if (board[i][j] == '.') {
          if (on_a_battleship == true) { // got off battleship
            on_a_battleship = false;
            res += 1;
          } else { // still not on a battleship
            continue;
          }
        } else if (board[i][j] == 'X') {
          if (horizontally_aligned) {
            if (on_a_battleship == true) { // still on a battleship
              continue;
            } else { // got on a battleship
              on_a_battleship = true;
            }
          } else { // hit a vertically aligned ship
            continue;
          }
        }
      }
    }
    res += static_cast<int>(on_a_battleship); // tally if still on the last ship

    // we overcount singletons, so modify tally
    int singletons = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        bool nothing_above = (i - 1 >= 0) ? (board[i - 1][j] == '.') : true;
        bool nothing_below = (i + 1 < m) ? (board[i + 1][j] == '.') : true;
        bool nothing_left = (j - 1 >= 0) ? (board[i][j - 1] == '.') : true;
        bool nothing_right = (j + 1 < n) ? (board[i][j + 1] == '.') : true;
        singletons +=
            static_cast<int>(board[i][j] == 'X' && nothing_above &&
                             nothing_below && nothing_left && nothing_right);
      }
    }
    res -= singletons;

    // final result
    return res;
  }
};
