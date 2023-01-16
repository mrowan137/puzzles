// Runtime: 0 ms (Beats 100%)
// Memory: 6.4 MB (Beats 87.4%)
class Solution {
 public:
  void printLinkedListInReverse(ImmutableListNode* head) {
    if (!head) return;
    printLinkedListInReverse(head->getNext());
    head->printValue();
  }
};
