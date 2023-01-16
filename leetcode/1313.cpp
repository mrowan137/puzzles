// Runtime: 3 ms, faster than 94.46% of C++ online submissions for Decompress Run-Length Encoded List.
// Memory Usage: 10.1 MB, less than 44.81% of C++ online submissions for Decompress Run-Length Encoded List.
class Solution {
public:
  vector<int> decompressRLElist(vector<int> &nums) {
    vector<int> res = {};
    for (int i = 0; i < nums.size() / 2; ++i) {
      int freq = nums[2 * i], value = nums[2 * i + 1];
      for (int j = 0; j < freq; ++j)
        res.push_back(value);
    }

    return res;
  }
};
