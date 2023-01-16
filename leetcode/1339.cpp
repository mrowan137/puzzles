// Runtime: 457 ms, faster than 5.27% of C++ online submissions for Maximum Product of Splitted Binary Tree.
// Memory Usage: 119.6 MB, less than 5.27% of C++ online submissions for Maximum Product of Splitted Binary Tree.
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
class Solution {
 public:
  long FindMaxProduct(TreeNode *node, long total_sum,
                      std::map<TreeNode *, long> &node_to_sum) {
    if (node == nullptr) {
      return LONG_MIN;
    }
    long max_product_left = FindMaxProduct(node->left, total_sum, node_to_sum);
    long max_product_right =
        FindMaxProduct(node->right, total_sum, node_to_sum);
    long max_product_self = (total_sum - node_to_sum[node]) * node_to_sum[node];
    return std::max({max_product_left, max_product_right, max_product_self});
  }

  long NodeToSum(TreeNode *node, std::map<TreeNode *, long> &node_to_sum) {
    if (node == nullptr) {
      return 0;
    }
    long res = node->val + NodeToSum(node->left, node_to_sum) +
               NodeToSum(node->right, node_to_sum);
    node_to_sum[node] = res;
    return res;
  }

  int maxProduct(TreeNode *root) {
    // For each descendant, save the net sum
    std::map<TreeNode *, long> node_to_sum;
    long total_sum = NodeToSum(root, node_to_sum);

    // Recurse to get the max product
    return FindMaxProduct(root, total_sum, node_to_sum) % (int(1e9) + 7);
  }
};
