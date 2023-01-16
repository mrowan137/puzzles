"""
Runtime: 48 ms, faster than 86.18% of Python3 online submissions for Print in Order.
Memory Usage: 14.5 MB, less than 42.54% of Python3 online submissions for Print in Order.
"""
from threading import Lock


class Foo:
    def __init__(self):
        # make the lock
        self.firstDone = Lock()
        self.secondDone = Lock()

        # lock the lock
        self.firstDone.acquire()
        self.secondDone.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        # unlock the lock
        self.firstDone.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.firstDone:
            printSecond()
            self.secondDone.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.secondDone:
            printThird()
