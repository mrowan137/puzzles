// Runtime: 3 ms, faster than 83.21% of C++ online submissions for Relative Sort Array.
// Memory Usage: 7.8 MB, less than 62.30% of C++ online submissions for Relative Sort Array.
class Solution {
 public:
  vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    // given:
    //   arr1: collection of elements, superset of arr2
    //   arr2: distinct elements, and found in arr1
    //   arr1, arr2: elements are on [0, 1000], so if not
    //               in arr2 just add 1000 and compare!
    //
    // goal:
    //   sort arr1 to have same relative ordering as arr2,
    //   with elements not in arr2 put to the end
    //

    // sort arr1 elements according to arr2, pushing those not in arr2 to back
    map<int, int> kv;
    for (int i = 0; i < arr2.size(); ++i) kv[arr2[i]] = i;
    sort(arr1.begin(), arr1.end(),
         [&](const int& a, const int& b)->bool {
           return ( (kv.find(a) != kv.end() ? kv[a] : a + 1000)
                  < (kv.find(b) != kv.end() ? kv[b] : b + 1000) );
         });

    return arr1;
  }
};
