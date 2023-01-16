// Runtime: 57 ms, faster than 94.42% of C++ online submissions for Maximum Sum Circular Subarray.
// Memory Usage: 39.9 MB, less than 33.58% of C++ online submissions for Maximum Sum Circular Subarray.
// Same idea as TLE (below), but faster sum through dragging window
class Solution {
 public:
  int maxSubarraySumCircular(vector<int> &nums) {
    // let's assume max sum is no wrap around
    // if it is, return that sum
    // if it's not, return the total minus that
    // in other words, return whatever is bigger
    int theMax = INT_MIN;
    int theMin = INT_MAX;
    int currMax = 0;
    int currMin = 0;
    for (vector<int>::const_iterator it = nums.begin(); it != nums.end();
         ++it) {
      currMax = std::max(currMax + *it, *it);
      currMin = std::min(currMin + *it, *it);
      theMax = std::max(theMax, currMax);
      theMin = std::min(theMin, currMin);
    }
    // edge case: if max is no elements, choose the largest b/c can't be empty
    int total = std::accumulate(nums.begin(), nums.end(), 0);
    return theMin == total ? theMax : max(theMax, total - theMin);
  }
};

// TLE
class Solution {
 public:
  int maxSubarraySumCircular(vector<int> &nums) {
    // let's assume max sum is no wrap around
    // if it is, return that sum
    // if it's not, return the total minus that
    // in other words, return whatever is bigger
    // N^2 search for the sum
    int theMax = nums[0];
    int theMin = nums[0];
    for (vector<int>::const_iterator it1 = nums.begin(); it1 != nums.end();
         ++it1) {
      int s = *it1;
      theMax = std::max(theMax, s);
      theMin = std::min(theMin, s);
      for (vector<int>::const_iterator it2 = it1 + 1; it2 != nums.end();
           ++it2) {
        s += *it2;
        theMax = std::max(theMax, s);
        theMin = std::min(theMin, s);
      }
    }
    // edge case: if max is no elements, choose the largest b/c can't be empty
    int total = std::accumulate(nums.begin(), nums.end(), 0);
    return theMin == total ? theMax : max(theMax, total - theMin);
  }
};
