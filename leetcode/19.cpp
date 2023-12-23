// Runtime: 3 ms
// Memory Usage: 11.1 MB
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
 public:
  ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(1);
    dummy.next = head;

    // count length
    int num_nodes = -1;
    ListNode* curr = &dummy;
    while (curr != nullptr) {
      num_nodes += 1;
      curr = curr->next;
    }

    // iterate to deletion node - 1
    int i = -1;
    curr = &dummy;
    while (num_nodes - i - 1 != n) {
      curr = curr->next;
      ++i;
    }

    // curr points to n-1'th node
    ListNode* tmp = curr->next->next;
    delete curr->next;
    curr->next = tmp;
    
    return dummy.next;
  }
};
