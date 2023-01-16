// Runtime: 21 ms, faster than 59.07% of C++ online submissions for Evaluate Boolean Binary Tree.
// Memory Usage: 15.1 MB, less than 35.50% of C++ online submissions for Evaluate Boolean Binary Tree.
class Solution {
 public:
  bool evaluateTree(TreeNode *root) {
    if (!root) {
      return true;
    }
    if (!root->left && !root->right) {
      return static_cast<bool>(root->val);
    }
    return (root->val == 2)
               ? evaluateTree(root->left) | evaluateTree(root->right)
               : evaluateTree(root->left) & evaluateTree(root->right);
  }
};
