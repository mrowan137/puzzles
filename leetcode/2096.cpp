// Runtime: 220 ms, faster than 91.43% of C++ online submissions for
// Step-By-Step Directions From a Binary Tree Node to Another. Memory Usage:
// 113.8 MB, less than 75.40% of C++ online submissions for Step-By-Step
// Directions From a Binary Tree Node to Another.
class Solution {
 public:
  bool getPathToNode(const TreeNode *node, const int value, string &path) {
    // return path to the target node
    if (node and node->val == value) {
      return true;
    }
    if (node->left and getPathToNode(node->left, value, path)) {
      path.push_back('L');
      return true;
    } else if (node->right and getPathToNode(node->right, value, path)) {
      path.push_back('R');
      return true;
    }
    return false;
  }

  string getDirections(TreeNode *root, int startValue, int destValue) {
    // find the path to start
    string path_to_start;
    getPathToNode(root, startValue, path_to_start);

    // find the path to dest
    string path_to_dest;
    getPathToNode(root, destValue, path_to_dest);

    // remove the shared path
    while (!path_to_start.empty() && !path_to_dest.empty() &&
           path_to_start.back() == path_to_dest.back()) {
      path_to_start.pop_back();
      path_to_dest.pop_back();
    }

    // convert start path to a sequence of 'U' and reverse dest
    return string(path_to_start.size(), 'U') +
           string(path_to_dest.rbegin(), path_to_dest.rend());
  }
};

// Runtime: 1815 ms, faster than 5.03% of C++ online submissions for
// Step-By-Step Directions From a Binary Tree Node to Another. Memory Usage:
// 266.2 MB, less than 5.03% of C++ online submissions for Step-By-Step
// Directions From a Binary Tree Node to Another.
class Solution {
 public:
  const bool hasValue(const TreeNode *node, const int target,
                      std::map<int, bool> &memo) {
    if (node == nullptr) {
      return false;
    }
    if (memo.find(node->val) != memo.end())
      return memo[node->val];
    if (node->val == target) {
      memo[node->val] = true;
      return true;
    }
    bool res = (hasValue(node->left, target, memo) ||
                hasValue(node->right, target, memo));
    memo[node->val] = res;
    return res;
  }

  string getDirections(TreeNode *root, int startValue, int destValue) {
    // 1) find path to the start and dest from root
    // 2) remove the shared directions
    // 3) replace remaining start directons by 'U'

    // find path to start
    TreeNode *curr = root;
    TreeNode *prev = root;
    std::map<int, bool> memo = {};
    string path_to_start = "";
    while (hasValue(curr->left, startValue, memo) ||
           hasValue(curr->right, startValue, memo)) {
      prev = curr;
      curr = hasValue(curr->left, startValue, memo) ? curr->left : curr->right;
      path_to_start += hasValue(prev->left, destValue, memo) ? "L" : "R";
    }

    // find path to dest
    curr = root;
    prev = root;
    memo.clear();
    string path_to_dest = "";
    while (hasValue(curr->left, destValue, memo) ||
           hasValue(curr->right, destValue, memo)) {
      prev = curr;
      curr = hasValue(curr->left, destValue, memo) ? curr->left : curr->right;
      path_to_dest += hasValue(prev->left, destValue, memo) ? "L" : "R";
    }

    // remove shared
    while (path_to_start != "" && path_to_dest != "" &&
           path_to_start[0] == path_to_dest[0]) {
      path_to_start.erase(0, 1);
      path_to_dest.erase(0, 1);
    }

    path_to_start = string(path_to_start.size(), 'U');
    return path_to_start + path_to_dest;
  }
};
