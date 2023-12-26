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
// Runtime: 12 ms
// Memory Usage: 22 MB
class Solution {
 public:
  bool isValidBST(TreeNode* root, 
                  long min=static_cast<long>(INT_MIN) - 1,
                  long max=static_cast<long>(INT_MAX) + 1) {
    // What is a BST? A tree where each node satisfies property:
    // - node value is greater than each value in left subtree;
    // - node value is less than each value in right subtree;
    // - node value is within the valid range.
    // 1. base case: root nullptr, valid BST
    if (root == nullptr) return true;

    // 2. general: node is BST if
    //   - left is BST
    bool left_is_valid_bst = isValidBST(root->left, 
                                        min, 
                                        std::min(static_cast<long>(root->val), max));

    //   - right is BST
    bool right_is_valid_bst = isValidBST(root->right,
                                         std::max(static_cast<long>(root->val), min),
                                         max);

    //   - left_max < node.value < right_min, and
    bool curr_gt_min_lt_max = (min < root->val && root->val < max);

    return left_is_valid_bst && right_is_valid_bst && curr_gt_min_lt_max;
    }
};
