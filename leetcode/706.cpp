// Runtime: 381 ms, faster than 14.48% of C++ online submissions for Design HashMap.
// Memory Usage: 50.9 MB, less than 94.50% of C++ online submissions for Design HashMap.
struct Node {
  int key_;
  int value_;
  Node *next_;
  Node(int key, int value) : key_(key), value_(value), next_(nullptr) {}
};

class MyHashMap {
 public:
  Node *dummy_;

  MyHashMap() : dummy_(new Node(-1, -1)) {}

  void put(int key, int value) {
    Node *prv = dummy_;
    Node *tmp = dummy_->next_;
    while (tmp != nullptr) {
      if (tmp->key_ == key) {
        tmp->value_ = value;
        return;
      }
      prv = prv->next_;
      tmp = tmp->next_;
    }
    prv->next_ = new Node(key, value);
    return;
  }

  int get(int key) {
    Node *tmp = dummy_->next_;
    while (tmp != nullptr) {
      if (tmp->key_ == key) {
        return tmp->value_;
      }
      tmp = tmp->next_;
    }
    return -1;
  }

  void remove(int key) {
    Node *prv = dummy_;
    Node *tmp = dummy_->next_;
    while (tmp != nullptr) {
      if (tmp->key_ == key) {
        prv->next_ = tmp->next_;
        delete tmp;
        return;
      }
      tmp = tmp->next_;
      prv = prv->next_;
    }
    return;
  }
};
