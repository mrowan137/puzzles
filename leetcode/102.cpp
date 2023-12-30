// Runtime: 7 ms
// Memory Usage: 15.4 MB
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
  void traverse(TreeNode* root, vector<vector<int>>& levels, int depth = 0) {
    if (root == nullptr) return;
    if (depth >= levels.size()) {
      levels.push_back(vector<int>());
    }
    levels[depth].push_back(root->val);
    traverse(root->left, levels, depth + 1);
    traverse(root->right, levels, depth + 1);
    return;
  }

  vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> levels = {};
    traverse(root, levels);
    return levels;
  }
};
