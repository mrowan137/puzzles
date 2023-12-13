// Runtime: 7 ms
// Memory Usage: 15.1 MB
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
  ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* dummy = new ListNode(-1);
    ListNode* curr = dummy;
    while (list1 != nullptr && list2 != nullptr) {
      if (list1->val < list2->val) {
        curr->next = list1;
        list1 = list1->next;
      } else {
        curr->next = list2;
        list2 = list2->next;
      } 
      curr = curr->next;
    }
    curr->next = list1 != nullptr? list1 : list2;
    return dummy->next;
  }
};

// Runtime: 15 ms, faster than 35.22% of C++ online submissions for Merge Two Sorted Lists.
// Memory Usage: 14.9 MB, less than 42.51% of C++ online submissions for Merge Two Sorted Lists.
class Solution {
 public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    // given:
    //   - 2 linked lists, sorted
    //
    // goal:
    //   - combining the linked lists into single sorted
    //   - don't want to allocate extra memory
    //
    // approach:
    //   - track the tail of the sorted list
    //   - from list1, list2, see which value is closer and add it
    //   - increment the tail, and whichever list1 list2 was added

    // every value will be greater than dummy head
    ListNode *dummy = new ListNode(-101);
    ListNode *curr = dummy;

    while (list1 != nullptr && list2 != nullptr) {
      if ((list1->val - curr->val) < (list2->val - curr->val)) {
        curr->next = list1;
        list1 = list1->next;
        curr = curr->next;
      } else {
        curr->next = list2;
        list2 = list2->next;
        curr = curr->next;
      }
    }
    curr->next = list1 != nullptr ? list1 : list2;

    return dummy->next;
  }
};
