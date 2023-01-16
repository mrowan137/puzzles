// Runtime: 222 ms (beats 98.23%)
// Memory: 97.2 MB (beats 19.23%)
class RandomizedSet {
 private:
  std::vector<int> values;
  std::map<int, int> valToKey;

 public:
  RandomizedSet() {
    // 2 data structure:
    //   - vector of all values
    //   - map from value --> key in the vector
  }

  bool insert(int val) {
    // valu not present
    if (valToKey.find(val) == valToKey.end()) {
      valToKey[val] = values.size();
      values.push_back(val);
      return true;
    }

    // val present
    return false;
  }

  bool remove(int val) {
    // val present
    if (valToKey.find(val) != valToKey.end()) {
      // move to erase spot, get the new idx
      values[valToKey[val]] = values[values.size() - 1];
      valToKey[values[values.size() - 1]] = valToKey[val];
      values.pop_back();
      valToKey.erase(val);
      return true;
    }

    // val not present
    return false;
  }

  int getRandom() { return values[rand() % values.size()]; }
};
