/**
 * // This is the ImmutableListNode's API interface.
 * // You should not implement it, or speculate about its implementation.
 * class ImmutableListNode {
 * public:
 *    void printValue(); // print the value of the node.
 *    ImmutableListNode* getNext(); // return the next node.
 * };
 */

// Runtime: 4 ms, faster than 60.30% of C++ online submissions for Print Immutable Linked List in Reverse.
// Memory Usage: 6.5 MB, less than 89.60% of C++ online submissions for Print Immutable Linked List in Reverse.
// O(log(N)) space at any one time because
//           recursion stack divide list in two
// O(N log(N)) time because we traverse N path
//             of size log(N) in getting to print value
class Solution {
 public:
  void printLinkedListInReverse(ImmutableListNode* head) {
    helper(head, NULL);
  }

  void helper(ImmutableListNode* start, ImmutableListNode* end) {
    // nothing to do if range is a single node, or start at the end
    if (start == NULL || start == end) { return; }
    // print out my value when the list was pared down to neighbors
    if (start->getNext() == end) {
      start->printValue();
      return;
    }

    ImmutableListNode* slow = start, *fast = start;

    // divide the list in two, [start, slow] + [slow, end]
    // and recurse on each half
    while (fast != end && fast->getNext() != end) {
      slow = slow->getNext();
      fast = fast->getNext()->getNext();
    }

    // now slow is the mid way of start, end
    helper(slow, end);
    helper(start, slow);
  }
};


// Runtime: 4 ms, faster than 61.16% of C++ online submissions for Print Immutable Linked List in Reverse.
// Memory Usage: 6.4 MB, less than 89.90% of C++ online submissions for Print Immutable Linked List in Reverse.
// O(1) space, O(N^2) time
class Solution {
 public:
  void printLinkedListInReverse(ImmutableListNode* head) {
    // save head
    ImmutableListNode* save = head;

    // go to the end of the list
    while (head->getNext()) {head = head->getNext();}

    // now we are at H-->END
    while (head != save) {
      // print the value
      head->printValue();

      // find the one before head & adjust head
      ImmutableListNode* tmp = save;
      while (tmp->getNext() != head) {tmp = tmp->getNext();}
      head = tmp;
    }

    // print the final value
    head->printValue();
  }
};

// recursion O(N) time, O(N) space
class Solution {
 public:
  void printLinkedListInReverse(ImmutableListNode* head) {
    if (head == nullptr) {return;}

    this->printLinkedListInReverse(head->getNext());
    head->printValue();
  }
};
