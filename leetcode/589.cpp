// Runtime: 29 ms, faster than 64.49% of C++ online submissions for N-ary Tree Preorder Traversal.
// Memory Usage: 11.2 MB, less than 77.97% of C++ online submissions for N-ary Tree Preorder Traversal.
//
// Definition for a Node.
// class Node {
// public:
//     int val;
//     vector<Node*> children;
//
//     Node() {}
//
//     Node(int _val) {
//         val = _val;
//     }
//
//     Node(int _val, vector<Node*> _children) {
//         val = _val;
//         children = _children;
//     }
// };
class Solution {
 public:
  void PreorderFromNary(Node *n, vector<int> &preorder) {
    // exit
    if (n == nullptr) {
      return;
    }

    preorder.push_back(n->val);
    for (auto c : n->children) {
      PreorderFromNary(c, preorder);
    }
  }
  vector<int> preorder(Node *root) {
    // given:
    //   - N-ary tree: consists of node values in order of levels;
    //     access children nodes with root->children --> vector<Node*>
    // find:
    //   - 'pre-order traversal' ~= 'explore all the way to the left,
    //     then backtrack up and explore the right'
    vector<int> res = {};
    PreorderFromNary(root, res);
    return res;
  }
};
