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
// Runtime: 4 ms, faster than 40.14% of C++ online submissions for Find Leaves of Binary Tree.
// Memory Usage: 8.9 MB, less than 45.89% of C++ online submissions for Find Leaves of Binary Tree.
class Solution {
 public:
  int getHeight(TreeNode *root, vector<vector<int>> &res) {
    if (!root) {
      return -1;
    }
    int left_height = getHeight(root->left, res);
    int right_height = getHeight(root->right, res);
    int h = 1 + max(left_height, right_height);
    if (res.size() <= h) {
      res.push_back({});
    }
    res[h].push_back(root->val);

    return h;
  }

  vector<vector<int>> findLeaves(TreeNode *root) {
    // key insight: measuring from bottom, leaves removed together have the same
    // height use recursion to calculate height of any node, and add it to the
    // vector for that height
    vector<vector<int>> res = {};
    getHeight(root, res);
    return res;
  }
};

// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Find Leaves of Binary Tree.
// Memory Usage: 9.2 MB, less than 7.95% of C++ online submissions for Find Leaves of Binary Tree.
class Solution {
 public:
  /* Helper function to get leaves of a given root */
  vector<int> getLeavesAndRemove(TreeNode **root) {
    if (*root == nullptr) {
      return vector<int>{};
    }
    if ((*root)->left == nullptr && (*root)->right == nullptr) {
      int tmp = (*root)->val;
      *root = nullptr; // assuming memory cleanup done somewhere else
      return vector<int>({tmp});
    }

    vector<int> res = {};
    vector<int> left_leaves = getLeavesAndRemove(&((*root)->left));
    vector<int> right_leaves = getLeavesAndRemove(&((*root)->right));
    res.reserve(left_leaves.size() + right_leaves.size());
    res.insert(res.end(), left_leaves.begin(), left_leaves.end());
    res.insert(res.end(), right_leaves.begin(), right_leaves.end());
    return res;
  }

  vector<vector<int>> findLeaves(TreeNode *root) {
    vector<vector<int>> res{};
    // Get all the leaves and remove them until no more leaves
    while (root) {
      res.push_back(getLeavesAndRemove(&root));
    }
    return res;
  }
};
