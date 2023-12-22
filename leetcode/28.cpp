// Runtime: 0 ms
// Memory Usage: 6.7 MB
class Solution {
 public:
  int strStr(string haystack, string needle) {
    for (string::const_iterator it = haystack.begin();
         it < haystack.end() - needle.size() + 1;
         ++it
    ) {
      string::const_iterator nit = needle.begin(), hit = it;
      while (nit != needle.end()
        && hit != haystack.end()
        && *hit == *nit
      ) {
        if (*nit != *hit) break;
        ++hit;
        ++nit;
      }
      if (nit == needle.end()) {
        return std::distance(
          static_cast<string::const_iterator>(haystack.begin()),
          it);
      }
    }
    return -1;
  }
};
