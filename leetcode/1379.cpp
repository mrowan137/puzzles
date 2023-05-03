// Runtime: 633 ms (Beats 5.9%)
// Memory: 163.8 MB (Beats 84.85%)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
 public:
  TreeNode *getTargetCopy(TreeNode *original, TreeNode *cloned,
                          TreeNode *target) {
    if (!original)
      return nullptr;

    if (target == original)
      return cloned;

    TreeNode *l = getTargetCopy(original->left, cloned->left, target);
    TreeNode *r = getTargetCopy(original->right, cloned->right, target);
    TreeNode *res = l ? l : r;

    return res;
  }
};
