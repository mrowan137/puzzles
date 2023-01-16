// Runtime: 34 ms, faster than 5.22% of C++ online submissions for Reverse Linked List.
// Memory Usage: 8.5 MB, less than 10.70% of C++ online submissions for Reverse Linked List.
// iterative, in-place
class Solution {
 public:
  ListNode *reverseList(ListNode *head) {
    ListNode *reversed = nullptr;
    while (head) {
      ListNode *next = head->next;
      head->next = reversed;
      reversed = head;
      head = next;
    }
    return reversed;
  }
};

// recursive
class Solution {
 public:
  ListNode *reverseList(ListNode *head) {
    // base case: nothing to reverse
    if (!head || !head->next) {
      return head;
    }

    // get reverse list, append me, return reverse
    ListNode *reverse = reverseList(head->next);
    ListNode *tmp = reverse;
    while (tmp && tmp->next) {
      tmp = tmp->next;
    }
    tmp->next = head;
    head->next = nullptr;
    return reverse;
  }
};
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
