// Runtime: 134 ms, faster than 22.30% of C++ online submissions for Logger Rate Limiter.
// Memory Usage: 32.4 MB, less than 86.32% of C++ online submissions for Logger Rate Limiter.
// Time: O(1) for lookup Space: O(N) to store the
// messages, where N is size of all incoming messages
class Logger {
 public:
  map<string, unsigned int> message_to_timestamp;

  Logger() : message_to_timestamp({}) {}

  bool shouldPrintMessage(unsigned int timestamp, string message) {
    if (message_to_timestamp.find(message) == message_to_timestamp.end()) {
      message_to_timestamp[message] = timestamp;
      return true;
    }

    if (timestamp - message_to_timestamp[message] >= 10) {
      message_to_timestamp[message] = timestamp;
      return true;
    }

    return false;
  }
};

// Runtime: 103 ms, faster than 52.67% of C++ online submissions for Logger Rate Limiter.
// Memory Usage: 35.8 MB, less than 5.85% of C++ online submissions for Logger Rate Limiter.
// Time: O(N), with N the size of queue; could need to cleanup all the old messages
// Space: O(2N), with N the size of incoming messages; factor 2 because set and deque
class Logger {
 public:
  unordered_set<string> messages_;
  deque<pair<string, unsigned int>> queue_;

  Logger() : messages_({}), queue_({}) {}

  bool shouldPrintMessage(unsigned int timestamp, string message) {
    // remove anything seen 10 or more seconds ago
    while (!queue_.empty() && (timestamp - queue_.back().second) >= 10) {
      messages_.erase(queue_.back().first);
      queue_.pop_back();
    }

    // print only if not seen in last 10 seconds
    bool res = false;
    if (messages_.find(message) == messages_.end()) {
      messages_.insert(message);
      queue_.push_front(pair<string, unsigned int>(message, timestamp));
      res = true;
    }

    return res;
  }
};
