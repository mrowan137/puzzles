// Runtime: 11 ms, faster than 92.81% of C++ online submissions for Destination City.
// Memory Usage: 10.5 MB, less than 91.95% of C++ online submissions for Destination City.
class Solution {
 public:
  string destCity(vector<vector<string>> &paths) {
    // let's create map from city to city
    // and then follow through and start city to the end
    // O(N*2) memory (dictionary of two pairs)
    // O(N) following through the longest path

    // store the edges
    map<string_view, string_view> city_to_city = {};
    for (const auto &p : paths)
      city_to_city[p[0]] = p[1];

    // follow through from any starting point
    string res = paths[0][0];
    while (city_to_city.find(res) != city_to_city.end())
      res = city_to_city[res];
    return res;
  }
};
