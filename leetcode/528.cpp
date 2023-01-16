// Runtime: 405 ms, faster than 14.72% of C++ online submissions for Random Pick with Weight.
// Memory Usage: 40.7 MB, less than 9.45% of C++ online submissions for Random Pick with Weight.
class Solution {

  vector<pair<float, int>> cdf;

 public:
  Solution(const vector<int> &w) {
    // let's divide up the unit interval in proportion to weights
    // then draw a random number on [0, 1];
    // compute the CDF
    float pCumul = 0.0;
    float totalSum = std::accumulate(w.begin(), w.end(), 0.0);
    vector<int>::size_type idx = 0;
    for (vector<int>::const_iterator it = w.begin(); it != w.end(); ++it) {
      pCumul += (*it) / totalSum;
      cdf.push_back(pair<float, int>(pCumul, idx++));
    }
  }

  int pickIndex() {
    float r = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
    vector<pair<float, int>>::const_iterator curr = cdf.begin(), prev;

    while (curr != cdf.end() && curr->first < r) {
      prev = curr++;
    }
    return curr != cdf.end() ? curr->second : prev->second;
  }
};
