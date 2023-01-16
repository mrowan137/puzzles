// Runtime: 235 ms, faster than 25.48% of C++ online submissions for Maximum Units on a Truck.
// Memory Usage: 16 MB, less than 53.04% of C++ online submissions for Maximum Units on a Truck.
class Solution {
 public:
  int maximumUnits(vector<vector<int>> &boxTypes, int truckSize) {
    // given:
    //   - vector of [number of boxes, units per box]
    //   - truck size in terms of boxes
    //
    // find:
    //   - max number of units we can pack into the truck
    //
    // insight:
    //   - fill truck with boxes that carry the most units until depleted
    //   - we can sort by the second argument then pop until done
    sort(
        boxTypes.begin(), boxTypes.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[1] > b[1]; });

    int res = 0, boxes_used = 0, i = 0;
    while (boxes_used < truckSize && i < boxTypes.size()) {
      i += boxTypes[i][0] == 0;
      if (i == boxTypes.size()) {
        break;
      }
      res += boxTypes[i][1];
      boxTypes[i][0] -= 1;
      boxes_used += 1;
    }

    return res;
  }
};
