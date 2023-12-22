// Runtime: 4 ms
// Memory Usage: 8.2 MB
class Solution {
 public:
  void deleteNode(ListNode* node) {
    if (node->next->next == nullptr) {
      node->val = node->next->val;
      delete node->next;
      node->next = nullptr;
      return;
    }
    node->val = node->next->val;
    deleteNode(node->next);
    return;
  }
};
