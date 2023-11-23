// Runtime: 7 ms
// Memory Usage: 18.8 MB
class Solution {
 public:
    int removeDuplicates(vector<int>& nums) {
        // two pointer approach
        int i = 0, j = 0;

        // i writes the non-duplicate value
        // j reads non-duplicate value
        while (j < nums.size()) {
            // j points to non-duplicate value
            nums[i] = nums[j];

            // point i to the next write location
            i += 1;

            // increment j to the next non-duplicate
            j += 1;
            while (j < nums.size() && nums[j] == nums[j-1]) {
                j += 1;
            }
        }

        return i;
    }
};
