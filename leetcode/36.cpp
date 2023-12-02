// Runtime: 18 ms
// Memory Usage: 20.9 MB
class Solution {
 public:
  const int rows = 9, cols = 9;

  std::pair<int, int> mapBlockToBoardCoords(int block, int i, int j) {
    int row = block;
    int col = i * 3 + j;
    return {row, col};
  }

  std::pair<int, int> relabelBlockToBoardCoords(int block, int i, int j) {
    const int row = (block / 3) * 3 + i;
    const int col = (block % 3) * 3 + j;
    return {row, col};
  }

  bool noDuplicates(const vector<char>& chunk) {
    std::unordered_map<char, int> count;
    for (auto el : chunk) {
      if (el == '.') continue;
      count[el] += 1;
    }

    for (auto pair : count) {
      if (pair.second > 1) return false;
    }

    return true;
  }

  bool isValidRows(const vector<vector<char>>& board) {
    for (int i = 0; i < rows; ++i) {
      if (!noDuplicates(board[i])) return false;
    }
    return true;
  }

  bool isValidBlocks(const vector<vector<char>>& board) {
    return true;
  }

  vector<vector<char>> transpose(const vector<vector<char>>& board) {
    vector<vector<char>> res = vector<vector<char>>(board);
    for (int i = 0; i < rows; ++i) {
      for (int j = i + 1; j < cols; ++j) {
        std::swap(res[i][j], res[j][i]);
      }
    }
    return res;
  }

  vector<vector<char>> reformatted(const vector<vector<char>>& board) {
    vector<vector<char>> res = vector<vector<char>>(board);

    for (int block = 0; block < 9; ++block) {
      for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
          const auto [x, y] = mapBlockToBoardCoords(block, i, j);
          const auto [a, b] = relabelBlockToBoardCoords(block, i, j);
          res[x][y] = board[a][b];
        }
      }
    }

    return res;
  }

  bool isValidSudoku(vector<vector<char>>& board) {
    // check valid rows
    if (!isValidRows(board)) return false;

    // check valid cols, i.e. rows in the transpose
    vector<vector<char>> board_transpose = transpose(board);
    if (!isValidRows(board_transpose)) return false;

    // check valid blocks, i.e. rows in the reformatted
    vector<vector<char>> board_reformatted = reformatted(board);
    if (!isValidRows(board_reformatted)) return false;

    return true;
  }
};
