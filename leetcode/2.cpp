// Runtime: 36 ms, faster than 81.30% of C++ online submissions for Add Two Numbers.
// Memory Usage: 71.5 MB, less than 12.12% of C++ online submissions for Add Two Numbers.
// cleaner solution
class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode *head = new ListNode(-1);
    ListNode *curr = head;
    int add, s, carry = 0;

    while (l1 != nullptr || l2 != nullptr) {
      curr->next = new ListNode;
      curr = curr->next;
      s = 0;
      if (l1 != nullptr) {
        s += l1->val;
        l1 = l1->next;
      }
      if (l2 != nullptr) {
        s += l2->val;
        l2 = l2->next;
      }
      s += carry;
      add = s % 10;
      carry = s / 10;

      curr->val = add;
    }

    if (carry != 0) {
      curr->next = new ListNode;
      curr = curr->next;
      curr->val = carry;
    }

    return head->next;
  }
};

// Runtime: 47 ms, faster than 56.36% of C++ online submissions for Add Two Numbers.
// Memory Usage: 72.9 MB, less than 12.12% of C++ online submissions for Add Two Numbers.
class Solution {
 public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode *res = new ListNode;
    ListNode *res_head = res;
    int carry = 0;
    int s;
    while (l1 != nullptr && l2 != nullptr) {
      s = l1->val + l2->val + carry;
      res->val = s % 10;
      res->next = new ListNode;
      res = res->next;

      // prep for next round
      carry = s / 10;
      l1 = l1->next;
      l2 = l2->next;
    }

    // we finished summing up to the valid digits
    // there can remain a carry as well as digits of the longer number
    ListNode *carry_ptr = new ListNode;
    ListNode *carry_ptr_head = carry_ptr;
    while (carry != 0) {
      // push back value
      carry_ptr->val = carry % 10;

      // prep for next round
      carry /= 10;
      carry_ptr->next = new ListNode;
      carry_ptr = carry_ptr->next;
    }
    // remove the trailing 0
    ListNode *tmp = carry_ptr_head;
    while (tmp->next != nullptr && tmp->next->next != nullptr) {
      tmp = tmp->next;
    }
    delete tmp->next;
    tmp->next = nullptr;

    ListNode *pre = nullptr;
    if (carry_ptr_head->val != 0) {
      pre = carry_ptr_head;
    }
    if (l1 != nullptr) {
      pre = addTwoNumbers(l1, carry_ptr_head);
    }
    if (l2 != nullptr) {
      pre = addTwoNumbers(l2, carry_ptr_head);
    }

    while (pre != nullptr) {
      // push back the value
      res->val = pre->val;

      // prep for the next round
      pre = pre->next;
      res->next = new ListNode;
      res = res->next;
    }

    // final result remove the trailing 0
    tmp = res_head;
    while (tmp->next != nullptr && tmp->next->next != nullptr) {
      tmp = tmp->next;
    }
    delete tmp->next;
    tmp->next = nullptr;

    return res_head;
  }
};
