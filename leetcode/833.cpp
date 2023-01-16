// Runtime: 7 ms, faster than 68.12% of C++ online submissions for Find And Replace in String.
// Memory Usage: 13.8 MB, less than 10.15% of C++ online submissions for Find And Replace in String.
class Solution {
 public:
  string findReplaceString(string s, vector<int> &indices,
                           vector<string> &sources, vector<string> &targets) {
    // do the replacements from right to left
    // in that way we didn't mess up the index on the left
    vector<pair<int, int>> value_to_index;
    for (int i = 0; i < indices.size(); ++i) {
      value_to_index.emplace_back(pair<int, int>(indices[i], i));
    }
    sort(value_to_index.rbegin(), value_to_index.rend());

    for (auto kv : value_to_index) {
      // check for match; if so replace
      // kv->first  -- index into string
      // kv->second -- original position in indicies/sources/targets
      if (s.substr(kv.first, sources[kv.second].size()) == sources[kv.second]) {
        s = s.substr(0, kv.first) + targets[kv.second] +
            s.substr(kv.first + sources[kv.second].size());
      }
    }
    return s;
  }
};
