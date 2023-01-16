// Runtime: 1000 ms, faster than 19.78% of C++ online submissions for Maximum Number of Visible Points.
// Memory Usage: 183.2 MB, less than 27.26% of C++ online submissions for Maximum Number of Visible Points.
class Solution {
 public:
  int visiblePoints(vector<vector<int>> &points, int angle,
                    vector<int> &location) {
    // put the points to an angle
    double kPi = acos(-1.0);
    vector<double> angles = {};
    int res1 = 0;
    int x0 = location[0], y0 = location[1];
    auto point_to_angle = [=](const int x, const int y) {
      return atan2(y - y0, x - x0) * 180 / kPi;
    };
    for (auto p : points) {
      int x = p[0], y = p[1];
      if (x == x0 && y == y0) {
        res1 += 1;
      } else {
        angles.emplace_back(point_to_angle(x, y));
      }
    }

    // sort them, repeat them +360 deg.
    sort(angles.begin(), angles.end());
    angles.insert(angles.end(), angles.begin(), angles.end());
    for (int i = angles.size() / 2; i < angles.size(); ++i) {
      angles[i] += 360;
    }

    // do a sliding window to find the max number of points
    int l = 0, res2 = 0;
    for (int r = 0; r < angles.size(); ++r) {
      if (angles[r] - angles[l] > angle) {
        ++l;
      }
      res2 = max(res2, r - l + 1);
    }

    return res1 + res2;
  }
};
