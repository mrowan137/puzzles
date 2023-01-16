// Runtime: 3 ms, faster than 60.90% of C++ online submissions for Binary Tree Preorder Traversal.
// Memory Usage: 9.4 MB, less than 12.96% of C++ online submissions for Binary Tree Preorder Traversal.
class Solution {
 public:
  vector<int> preorderTraversal(TreeNode *root) {
    if (!root) {
      return vector<int>();
    }
    vector<int> l = preorderTraversal(root->left);
    vector<int> r = preorderTraversal(root->right);
    vector<int> res;
    res.reserve(1 + l.size() + r.size());
    res.push_back(root->val);
    res.insert(res.end(), l.begin(), l.end());
    res.insert(res.end(), r.begin(), r.end());

    return res;
  }
};
