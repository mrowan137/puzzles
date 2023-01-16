// Runtime: 16 ms, faster than 55.14% of C++ online submissions for Maximum Number of Words Found in Sentences.
// Memory Usage: 9.7 MB, less than 94.52% of C++ online submissions for Maximum Number of Words Found in Sentences.
class Solution {
 public:
  int mostWordsFound(vector<string> &sentences) {
    int res = INT_MIN;
    for (vector<string>::const_iterator it_s = sentences.begin();
         it_s != sentences.end(); ++it_s) {
      int num_spaces = 0;
      for (string::const_iterator it_c = (*it_s).begin(); it_c != (*it_s).end();
           ++it_c) {
        num_spaces += (*it_c) == ' ' ? 1 : 0;
      }
      // number of words is 1 more than number of spaces
      res = max(res, num_spaces + 1);
    }
    return res;
  }
};
