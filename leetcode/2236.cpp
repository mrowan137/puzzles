// Runtime: 4 ms, faster than 48.99% of C++ online submissions for Root Equals Sum of Children.
// Memory Usage: 12.6 MB, less than 69.42% of C++ online submissions for Root Equals Sum of Children.
class Solution {
 public:
  bool checkTree(TreeNode *root) {
    return root->val == root->left->val + root->right->val;
  }
};
