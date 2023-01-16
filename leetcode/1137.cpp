// Runtime: 0 ms (beats 100%)
// Memory: 6 MB (beats 36.35%)
// recursion with a template
template <int n> class Tribonacci {
 public:
  constexpr static int res = (Tribonacci<n - 1>::res + Tribonacci<n - 2>::res +
                              Tribonacci<n - 3>::res);
  Tribonacci<n - 1> lowerTrib;
  constexpr int operator[](int i) { return i == n ? res : lowerTrib[i]; }
};

// base cases for 0, 1, 2
template <> class Tribonacci<0> {
 public:
  constexpr static int res = 0;
  constexpr int operator[](int i) { return res; }
};

template <> class Tribonacci<1> {
 public:
  constexpr static int res = 1;
  Tribonacci<0> lowerTrib;
  constexpr int operator[](int i) { return i == 1 ? res : lowerTrib[i]; }
};

template <> class Tribonacci<2> {
 public:
  constexpr static int res = Tribonacci<1>::res + Tribonacci<0>::res;
  Tribonacci<1> lowerTrib;
  constexpr int operator[](int i) { return i == 2 ? res : lowerTrib[i]; }
};

Tribonacci<37> t;

class Solution {
 public:
  int tribonacci(int n) { return t[n]; }
};
