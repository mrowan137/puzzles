// Runtime: 29 ms, faster than 54.78% of C++ online submissions for Moving Average from Data Stream.
// Memory Usage: 14.4 MB, less than 5.77% of C++ online submissions for Moving Average from Data Stream.
struct linkedListNode {
  double val;
  linkedListNode *next;
  linkedListNode(double v) : val(v), next(nullptr) {}
};

class MovingAverage {
 private:
  int windowSize, length;
  double movingAvg;
  linkedListNode *head, *curr;

 public:
  MovingAverage(int size)
      : head(new linkedListNode(-1)), curr(new linkedListNode(-1)),
        windowSize(size), length(0), movingAvg(0) {
    head->next = curr;
  }

  double next(int val) {
    // fill the current node, queue the next dummy
    curr->val = val;
    curr->next = new linkedListNode(-1);
    curr = curr->next;

    // new avg is weighted sum of prv, and the new value
    // avg = old*n/(n + 1) + new*1/(n + 1)
    movingAvg *= length / (length + 1.);
    movingAvg += val / (length + 1.);
    length += 1;

    // the list might be too large
    if (length > windowSize) {
      // moving average no longer needs oldest value
      movingAvg -= head->next->val / (length);
      movingAvg *= length / (length - 1.);

      // remove oldest value from linked list
      linkedListNode *tmp = head->next;
      head->next = head->next->next;
      delete tmp;
      length -= 1;
    }
    return movingAvg;
  }
};
