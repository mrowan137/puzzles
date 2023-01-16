// Runtime: 408 ms, faster than 84.78% of C++ online submissions for Design SQL.
// Memory Usage: 145.9 MB, less than 50.73% of C++ online submissions for Design SQL.
class SQL {
 public:
  map<string, vector<vector<string>>> table;
  SQL(vector<string> &names, vector<int> &columns) {
    for (int i = 0; i < names.size(); ++i) {
      table[names[i]] = vector<vector<string>>({});
    }
  }

  void insertRow(string name, vector<string> row) {
    table[name].push_back(row);
  }

  void deleteRow(string name, int rowId) {
    // hack -- delete row should not change
    //         the id if the next row, so
    //         not deleting preserves the id;
    //         this works but not best for memory
    // table[name].erase(table[name].begin() + rowId);
  }

  string selectCell(string name, int rowId, int columnId) {
    return table[name][rowId - 1][columnId - 1];
  }
};
