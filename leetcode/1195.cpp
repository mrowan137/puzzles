// Runtime: 394 ms, faster than 5.13% of C++ online submissions for Fizz Buzz Multithreaded.
// Memory Usage: 6.7 MB, less than 58.11% of C++ online submissions for Fizz Buzz Multithreaded.

#define N 51

class FizzBuzz {
 private:
  int n;

 public:
  static bool* completed_;
  FizzBuzz(int n) {
    this->n = n;
    do {
      for (int i = 0; i < n; ++i) completed_[i] = false;
      completed_[N - 1] = true;
    } while (completed_[N - 1] == false);

    // all the threads agree
  }

  // printFizz() outputs "fizz".
  void fizz(function<void()> printFizz) {
    // i%3 == 0
    int i = 3;
    while (i <= n && completed_[n-1] == false) {
      if (completed_[i-2]) {
        printFizz();
        completed_[i-1] = true;
        i += 3;
        if (i%5 == 0) i += 3;
      }
    }
    if (i == n) completed_[N-1] = false;
  }

  // printBuzz() outputs "buzz".
  void buzz(function<void()> printBuzz) {
    // i%5 == 0
    int i = 5;
    while (i <= n && completed_[n-1] == false) {
      if (completed_[i-2]) {
        printBuzz();
        completed_[i-1] = true;
        i += 5;
        if (i%3 == 0) i += 5;
      }
    }
    if (i == n) completed_[N-1] = false;
  }

  // printFizzBuzz() outputs "fizzbuzz".
  void fizzbuzz(function<void()> printFizzBuzz) {
    // i%3 == 0 && i%5 == 0
    int i = 3;
    while (i <= n && completed_[n-1] == false) {  // as long as work to do
      if (i%3 == 0 && i%5 == 0) {  // we can do some work
        if (completed_[i-2]) {  // but only if previous has completed
          printFizzBuzz();
          completed_[i-1] = true;
          i += 1;
        }
      } else {
        i += 1;
      }
    }
  if (i == n) completed_[N-1] = false;
  }

  // printNumber(x) outputs "x", where x is an integer.
  void number(function<void(int)> printNumber) {
    // i%3 != 0 && i%5 != 0
    int i = 1;
    while (i <= n && completed_[n-1] == false) {
      if (i%3 != 0 && i%5 != 0) {
        if ( i == 1 || (completed_[i-2] == true) ) {
          printNumber(i);
          completed_[i-1] = true;
          i += 1;
        }
      } else {
        i += 1;
      }
    }
  if (i == n) completed_[N-1] = false;
  }
};

// last digit is a flag for threads to
// synchronize when the array is reset
bool* FizzBuzz::completed_ = new bool[N]();
