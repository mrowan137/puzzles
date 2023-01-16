// Runtime: 365 ms, faster than 55.17% of C++ online submissions for Snapshot Array.
// Memory Usage: 87.5 MB, less than 91.07% of C++ online submissions for Snapshot Array.
// Big brain M Log(N) where N is the number of keys in map at an index
// and M is the number of get operations
class SnapshotArray {
 public:
  unordered_map<int, map<int, int> > snapshot_array_;
  int snap_id_;
  SnapshotArray(int length)
    : snapshot_array_({}), snap_id_(0) {}

  void set(int index, int val) { snapshot_array_[index][snap_id_] = val; }

  int snap() { return snap_id_++; }

  int get(int index, int snap_id) {
    auto it = snapshot_array_[index].upper_bound(snap_id);
    return it == snapshot_array_[index].begin() ? 0 : prev(it)->second;
  }
};

// TLE
class SnapshotArray {
 public:
  vector<map<int, int> > snapshot_array_;
  vector<int> tmp_;
  int snap_id_;
  SnapshotArray(int length)
    : snapshot_array_(length, map<int, int>()), snap_id_(0), tmp_(length, 0) {
    for (int i = 0; i < length; ++i) snapshot_array_[i][snap_id_] = tmp_[i];
  }

  void set(int index, int val) {
    tmp_[index] = val;
  }

  int snap() {
    for (int i = 0; i < tmp_.size(); ++i) {
      snapshot_array_[i][snap_id_] = tmp_[i];
    }
    snap_id_ += 1;
    return snap_id_ - 1;
  }

  int get(int index, int snap_id) {
    return snapshot_array_[index][snap_id];
  }
};
