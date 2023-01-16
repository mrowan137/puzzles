"""Find approximations M/N ~= pi where M and N are integers"""
from collections import defaultdict

N = 1001
pi = [
    "3",
    ".",
    "1",
    "4",
    "1",
    "5",
    "9",
    "2",
    "6",
    "5",
    "3",
    "5",
    "8",
    "9",
    "7",
    "9",
    "3",
    "2",
    "3",
    "8",
    "4",
    "6",
]


def find_matches(matches):
    for i in range(1, N):
        for j in range(1, N):
            n = list(str(1.0 * i / j))
            l = 0
            while l < len(pi) and l < len(n) and pi[l] == n[l]:
                l += 1
            matches[l].append((i, j))


if __name__ == "__main__":
    m = defaultdict(list)
    find_matches(m)
    print(
        "Best integer fraction i/j approximations for pi \n"
        "where 1 <= i <= 1000, 1 <= j <= 1000):\n"
    )
    for pair in m[max(m)]:
        print(
            "({} matches) {}/{} = {}".format(
                max(m), pair[0], pair[1], 1.0 * pair[0] / pair[1]
            )
        )

    print("                 pi = " + "".join(pi))
