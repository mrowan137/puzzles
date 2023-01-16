// Runtime: 8 ms, faster than 15.00% of C++ online submissions for Invert Binary Tree.
// Memory Usage: 9.8 MB, less than 38.33% of C++ online submissions for Invert Binary Tree.
class Solution {
 public:
  TreeNode *invertTree(TreeNode *root) {
    // base case
    if (!root) {
      return root;
    }

    // swap all the way down
    swap(root->left, root->right);
    invertTree(root->left);
    invertTree(root->right);
    return root;
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
