// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Middle of the Linked List.
// Memory Usage: 7.1 MB, less than 21.54% of C++ online submissions for Middle of the Linked List.
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
  ListNode *middleNode(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast->next != nullptr && fast->next->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
    }
    return fast->next == nullptr ? slow : slow->next;
  }
};
