// Runtime: 184 ms
// Memory Usage: 118.6 MB
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
  bool isPalindrome(ListNode* head) {
    if (head == nullptr) return true;

    // 1. find end of first half
    ListNode* first_half_end = FirstHalfEnd(head);

    // 2. find start of second half
    // 3. reverse second half and compare
    ListNode* second_half_start = ReverseLinkedList(first_half_end->next);
    bool res = true;
    ListNode* p1 = head;
    ListNode* p2 = second_half_start;
    while (p1 != nullptr && p2 != nullptr) {
      res &= p1->val == p2->val;
      p1 = p1->next;
      p2 = p2->next;
    }

    // 4. restore the second half
    first_half_end->next = ReverseLinkedList(second_half_start);
    return res;
  }

  ListNode* FirstHalfEnd(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast->next != nullptr && fast->next->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
    }
    return slow;
  }

  ListNode* ReverseLinkedList(ListNode* head) {
    ListNode* rev = nullptr;
    while (head != nullptr) {
      ListNode* nxt = head->next;
      head->next = rev;
      rev = head;
      head = nxt;
    }
    return rev;
  }
};
