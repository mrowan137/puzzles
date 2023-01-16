// Runtime: 39 ms, faster than 6.22% of C++ online submissions for Delete Node in a Linked List.
// Memory Usage: 7.7 MB, less than 39.02% of C++ online submissions for Delete Node in a Linked List.
class Solution {
 public:
  void deleteNode(ListNode *node) {
    node->val = (node->next)->val;
    if (!node->next->next) {
      node->next = nullptr;
      return;
    }
    deleteNode(node->next);
  }
};
