// Runtime: 4 ms (beats 35.22%)
// Memory: 6.2 MB (beats 85.15%)
class Solution {
 public:
  int countPoints(string rings) {
    // given:
    //   - n ring: R, G, B
    //   - 10 rods
    //   - 2n length string: "[color, position] [color, position] ..."
    //
    // find:
    //   - number of rods with all 3 colors
    //
    // approach:
    //   - initialize array to represent the 10 rods contents
    //   - hash the 3 colors: bitwise or
    //   - add the rings iteratively
    //   - if rod has value 0x0007 = 0b0111, it means it has all 3 colors
    //     so we increment the count

    int rod_contents[10] = {0};
    int count = 0;
    const int n = rings.size() / 2;

    auto ColorToValue = [=](char c) {
      if (c == 'R') {
        return 0x0001; // 0b 0001
      } else if (c == 'G') {
        return 0x0002; // 0b 0010
      } else if (c == 'B') {
        return 0x0004; // 0b 0100
      }
      return 0x0000;
    };

    for (int i = 0; i < n; ++i) {
      char c = rings[2 * i];
      int p = rings[2 * i + 1] - int('0');
      rod_contents[p] |= ColorToValue(c);

      // increment if all 3 rings
      count += rod_contents[p] == 0x0007 ? 0x0001 : 0x0000;

      // flag with 0b1111 to ignore if it had all rings
      rod_contents[p] = rod_contents[p] == 0x0007 ? 0x000F : rod_contents[p];
    }

    return count;
  }
};
