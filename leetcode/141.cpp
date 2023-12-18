// Runtime: 7 ms
// Memory Usage: 8.4 MB
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  bool hasCycle(ListNode *head) {
    if (head == nullptr) return false;

    ListNode* slow = head;
    ListNode* fast = head;
    unsigned int cnt = 0;
    while ( (slow != fast || cnt == 0)
            && fast->next != nullptr && fast->next->next != nullptr
            && cnt < 10000) {
      slow = slow->next;
      fast = fast->next->next;
      cnt += 1;
    }
    return (0 < cnt) && (cnt < 10000) && (fast == slow);
  }
};
