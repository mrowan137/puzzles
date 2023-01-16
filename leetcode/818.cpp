// Runtime: 15 ms, faster than 72.40% of C++ online submissions for Race Car.
// Memory Usage: 8.2 MB, less than 61.54% of C++ online submissions for Race Car.
struct PairHash {
  template <typename T1, typename T2>
  size_t operator()(const pair<T1, T2> &pair) const {
    return hash<T1>()(pair.first) ^ hash<T2>()(pair.second);
  }
};

struct State {
  int position_;
  int speed_;
  int num_instructions_;
  explicit State(int x, int s, int n) noexcept
      : position_(x), speed_(s), num_instructions_(n) {}
};

class Solution {
 public:
  int racecar(int target) {
    // given:
    //   - initial [x, s] = [0, 1]
    //   - A: positions += speed
    //        speed *= 2
    //   - R: speed = s > 0 ? -1 : 1
    // goal:
    //   - reach a target position in shortest possible instructions
    //
    deque<State> states = {State(0, 1, 0)};
    unordered_set<pair<int, int>, PairHash> seen = {};
    while (!states.empty()) {
      State curr = states[0];
      states.pop_front();

      // exit if we hit the target
      if (curr.position_ == target) {
        return curr.num_instructions_;
      }

      // generate all possible new states
      State acc = State(curr.position_ + curr.speed_, curr.speed_ * 2,
                        curr.num_instructions_ + 1);
      State rev = State(curr.position_, curr.speed_ > 0 ? -1 : 1,
                        curr.num_instructions_ + 1);

      // position must be less than half target or it will overflow next step
      if (seen.find(pair(acc.position_, acc.speed_)) == seen.end() &&
          abs(acc.position_) < 2 * target) {
        seen.insert(pair(acc.position_, acc.speed_));
        states.push_back(acc);
      }

      // only consider to change direction if next step is moving away
      if (seen.find(pair(rev.position_, rev.speed_)) == seen.end() &&
          (acc.position_ > target && curr.speed_ > 0 ||
           acc.position_ < target && curr.speed_ < 0)) {
        seen.insert(pair(rev.position_, rev.speed_));
        states.push_back(rev);
      }
    }

    return -1;
  }
};
