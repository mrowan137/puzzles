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
// Runtime: 0 ms
// Memory Usage: 19.1 MB
class Solution {
 public:
  int maxDepth(TreeNode* root) {
    // 1. base case
    if (root == nullptr) return 0;

    // 2. non-nullptr root
    //   - compare left and right roots' max depth, return max + 1
    unsigned int max_depth = std::max(maxDepth(root->left),
                                      maxDepth(root->right));
    return max_depth + 1;
  }
};

// Runtime: 17 ms, faster than 32.41% of C++ online submissions for Maximum Depth of Binary Tree.
// Memory Usage: 19 MB, less than 14.19% of C++ online submissions for Maximum Depth of Binary Tree.
// BFS
class Solution {
 public:
  int maxDepth(TreeNode* root) {
    // store the node and it's height
    if (!root) return 0;
    deque<pair<TreeNode*, int>> d = {pair<TreeNode*, int>(root, 1)};
    using pair_type = decltype(d)::value_type;
    int res = INT_MIN;
    while (!d.empty()) {
      pair_type p = d[0];
      d.pop_front();
      if (p.first->left)  d.push_back(pair_type(p.first->left,  p.second + 1));
      if (p.first->right) d.push_back(pair_type(p.first->right, p.second + 1));
      res = max(res, p.second);
    }

    return res;
  }
};

