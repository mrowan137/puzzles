// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Univalued Binary Tree.
// Memory Usage: 10 MB, less than 8.19% of C++ online submissions for Univalued Binary Tree.
class Solution {
 public:
  bool isUnivalTree(TreeNode *root) {
    if (!root) {
      return true;
    }
    return (isUnivalTree(root->left) && isUnivalTree(root->right) &&
            (root->left ? root->left->val == root->val : true) &&
            (root->right ? root->right->val == root->val : true));
  }
};
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
