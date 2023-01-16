// Runtime: 753 ms, faster than 58.14% of C++ online submissions for Stock Price Fluctuation.
// Memory Usage: 164.1 MB, less than 83.33% of C++ online submissions for Stock Price Fluctuation.
//
//     x
//     x   x
//   x x x x x
//   x x x x x
//
//   min = 2, max = 4, last_timestamp = 4
//
//
//   what if want to update?  update(1, 1):
//
//
//         x
//   x   x x x
//   x x x x x
//
//   min = 1, max = 3, last_timestamp = 4
//
// why is unordered_map timestamp --> price, map price--> freq a natural idea?
// it's like we keep the timestamp, and a list of the prices:
//   prices map:     0: 2, 1:4, 2:2, 3:3, 4:2
//   ordered list of prices: 2,2,2,3,4
// list of prices can tell us the min, max in O(1) time
// for retroactive update, we pop from the list which would update our min, max
// and we can always get the current as the most recent timestamp in the map
class StockPrice {
 public:
  int last_timestamp;
  unordered_map<int, int> prices;
  map<int, int> freqs;

  StockPrice() : last_timestamp(0), prices({}), freqs({}) {}

  void update(int timestamp, int price) {
    last_timestamp = max(timestamp, last_timestamp);

    // if we get an old timestamp, update
    if (prices.find(timestamp) != prices.end()) {
      // update freqs
      int old_price = prices[timestamp];
      freqs[old_price] -= 1;
      if (freqs[old_price] == 0) {
        freqs.erase(old_price);
      }
    }
    // update the price
    prices[timestamp] = price;
    freqs[price] += 1;
  }

  int current() { return prices[last_timestamp]; }

  int maximum() { return freqs.rbegin()->first; }

  int minimum() { return freqs.begin()->first; }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
