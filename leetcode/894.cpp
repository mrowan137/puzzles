// Runtime: 109 ms, faster than 73.84% of C++ online submissions for All Possible Full Binary Trees.
// Memory Usage: 29.2 MB, less than 59.02% of C++ online submissions for All Possible Full Binary Trees.
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
 private:
  std::map<int, vector<TreeNode *>> n_to_treenode_;

 public:
  vector<TreeNode *> allPossibleFBT(int n) {
    if (n_to_treenode_.find(n) != n_to_treenode_.end()) {
      return n_to_treenode_[n];
    }
    // we can build the FBT recursively
    // for each FBT of size n-1, we build all size n FBT
    // by making the n-1 a left or right subtree
    if (n < 1) {
      return vector<TreeNode *>({});
    }
    if (n == 1) {
      return vector<TreeNode *>({new TreeNode});
    }

    vector<TreeNode *> res = {};

    for (int m = 1; m < n; m += 2) {
      vector<TreeNode *> subtrees_l_ptr = allPossibleFBT(m);
      vector<TreeNode *> subtrees_r_ptr = allPossibleFBT(n - m - 1);
      for (auto &subtree_l_ptr : subtrees_l_ptr) {
        for (auto &subtree_r_ptr : subtrees_r_ptr) {
          TreeNode *t_ptr = new TreeNode;
          t_ptr->left = subtree_l_ptr;
          t_ptr->right = subtree_r_ptr;
          res.push_back(t_ptr);
        }
      }
    }

    n_to_treenode_[n] = res;
    return res;
  }
};
