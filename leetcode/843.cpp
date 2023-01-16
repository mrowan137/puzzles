// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Guess the
// Word. Memory Usage: 6.3 MB, less than 93.89% of C++ online submissions for
// Guess the Word.
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
 public:
  void findSecretWord(vector<string> &wordlist, Master &master) {
    // given wordlist of 6 letter words
    // master.guess(word) gives integer representing matches (position + value)
    // need to guess the secret word (which is in the list) in few guesses
    auto NumMatches = [](const string_view &s1, const string_view &s2) {
      int res = 0;
      for (int i = 0; i < 6; ++i) {
        res += s1[i] == s2[i];
      }
      return res;
    };

    int guesses = 0, matches = 0;
    while (guesses < 10 && matches != 6) {
      srand(1);
      string trial_word = wordlist[rand() % wordlist.size()];
      matches = master.guess(trial_word);
      vector<string> candidates = {};
      for (auto w : wordlist) {
        if (w != trial_word && NumMatches(w, trial_word) == matches) {
          candidates.emplace_back(w);
        }
      }
      wordlist = candidates;
      guesses += 1;
    }
  }
};
