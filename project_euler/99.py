"""
Q: Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given
above.

A: 709
"""

from math import log


def largest_exponential(file_name):
    # read file
    base_exps = []
    with open(file_name) as f:
        for line in f:
            row = line.replace("\n", "").split(",")
            base_exps.append([int(x) for x in row])

    line_no, b_res_log_a_res, a_res, b_res = 0, float("-inf"), -1, -1
    for i, base_exp in enumerate(base_exps):
        a, b = base_exp
        new_b_log_a = max(b_res_log_a_res, b * log(a))
        if new_b_log_a > b_res_log_a_res:
            b_res_log_a_res = new_b_log_a
            a_res, b_res = a, b
            line_no = i + 1

    return line_no, a_res, b_res


if __name__ == "__main__":
    file_path = "./base_exp.txt"
    l, x, y = largest_exponential(file_path)
    print(
        "Largest exponential in {} is on line {} ({}^{})".format(
            file_path, l, x, y
        )
    )
