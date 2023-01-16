// Runtime: 598 ms, faster than 34.29% of C++ online submissions for Detect Squares.
// Memory Usage: 143.8 MB, less than 26.77% of C++ online submissions for Detect Squares.
class DetectSquares {
 public:
  // count the number of points at a location
  int point_to_count_[1001][1001];
  vector<pair<int, int>> points_;

  DetectSquares() : point_to_count_(), points_() {}

  void add(vector<int> point) {
    point_to_count_[point[0]][point[1]] += 1;
    points_.emplace_back(pair<int, int>(point[0], point[1]));
  }

  int count(vector<int> point) {
    int res = 0;

    // any point on the diagonal, we count the squares
    int x0 = point[0], y0 = point[1];
    for (auto &[x1, y1] : points_) {
      if (!(x1 - x0 == y1 - y0 || x1 - x0 == y0 - y1) || x1 - x0 == 0)
        continue;
      res += point_to_count_[x1][y0] * point_to_count_[x0][y1];
    }
    return res;
  }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
