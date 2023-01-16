// Runtime: 65 ms, faster than 31.55% of C++ online submissions for Group Anagrams.
// Memory Usage: 26.3 MB, less than 11.57% of C++ online submissions for Group Anagrams.
class Solution {
 public:
  vector<int> letterCount(const string &str) {
    vector<int> counts(26);
    fill(counts.begin(), counts.end(), 0);
    for (string::const_iterator it = str.begin(); it != str.end(); ++it) {
      counts[int(*it) - 97] += 1;
    }
    return counts;
  }

  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    // convenience
    typedef std::map<vector<int>, vector<string>> letterCountToStrings_t;

    // make a map from [n_a, n_b, ..., n_z] --> string
    letterCountToStrings_t letterCountToStrings;
    for (vector<string>::const_iterator it = strs.begin(); it != strs.end();
         ++it) {

      vector<int> counts = letterCount(*it);
      letterCountToStrings[counts].push_back(*it);
    }

    // get the final list of lists
    vector<vector<string>> groupedAnagrams;
    for (letterCountToStrings_t::const_iterator it =
             letterCountToStrings.begin();
         it != letterCountToStrings.end(); ++it) {
      groupedAnagrams.push_back(it->second);
    }

    return groupedAnagrams;
  }
};
