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
// Runtime: 7 ms
// Memory Usage: 8.8 MB
// iterative, in-place
class Solution {
 public:
  ListNode* reverseList(ListNode* head) {
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

// Runtime: 8 ms
// Memory Usage: 9.1 MB
// iterative, not in-place
class Solution {
 public:
  void Insert(ListNode* curr, ListNode* nxt) {
    ListNode* tmp = curr->next;
    curr->next = nxt;
    nxt->next = tmp;
    return;
  }
  ListNode* reverseList(ListNode* head) {
    ListNode* curr = head;
    ListNode* rev = new ListNode(-1);
    while (curr != nullptr) {
      ListNode* insert = new ListNode(curr->val);
      Insert(rev, insert);
      curr = curr->next;
    }
    return rev->next;
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
