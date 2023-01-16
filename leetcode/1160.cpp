// Runtime: 45 ms, faster than 98.25% of C++ online submissions for Find Words That Can Be Formed by Characters.
// Memory Usage: 17.7 MB, less than 79.87% of C++ online submissions for Find Words That Can Be Formed by Characters.
class Solution {
 public:
  int countCharacters(vector<string>& words, string chars) {
    // encode the letters we have available
    int available_char_count[26] = {0};
    for (auto c : chars) {
      available_char_count[static_cast<int>(c) - static_cast<int>('a')] += 1;
    }

    // Now check words available
    int res = 0;
    int word_char_count[26] = {0};
    for (auto word : words) {
      memset(word_char_count, 0, 26*sizeof(int));
      for (auto c : word) {
        word_char_count[static_cast<int>(c) - static_cast<int>('a')] += 1;
      }

      // Check if the word is possible
      bool flag_possible = true;
      for (int i = 0; i < 26; ++i) {
        if (available_char_count[i] - word_char_count[i] < 0) {
          flag_possible = false;
          break;
        }
      }

      res += flag_possible ? word.size() : 0;
    }

    return res;
  }
};
