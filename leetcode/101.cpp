// Runtime: 5 ms
// Memory Usage: 16.7 MB
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
 public:
  void mirrorTree(TreeNode* root) {
    // modify tree to be mirror version
    if (root == nullptr) return;
    TreeNode* swap = root->right;
    root->right = root->left;
    root->left = swap;
    mirrorTree(root->left);
    mirrorTree(root->right);
    return;
  }

  bool isEqual(TreeNode* r1, TreeNode* r2) {
    // check two treenodes are equal
    if (r1 == nullptr && r2 == nullptr) {
      return true;
    }

    if (r1 != nullptr && r2 == nullptr || r1 == nullptr && r2 != nullptr) {
      return false;
    }

    return (r1->val == r2->val
            && isEqual(r1->left, r2->left)
            && isEqual(r1->right, r2->right));
  }

  bool isSymmetric(TreeNode* root) {
    mirrorTree(root->left);
    bool res = isEqual(root->left, root->right);
    mirrorTree(root->right);
    return res;
  }
};
