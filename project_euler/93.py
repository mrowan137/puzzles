"""
Q: By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
making use of the four arithmetic operations (+, -, *, /) and
brackets/parentheses, it is possible to form different positive integer targets.

For example,
   8 = (4*(1 + 3)) / 2
  14 = 4*(3 + 1/2)
  19 = 4*(2 + 3) - 1
  36 = 3*4*(2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to n can be
obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set
of consecutive positive integers, 1 to n, can be obtained, giving your answer as
a string: abcd.

A: 1258
"""


from itertools import permutations

def apply_ops_rl(seq, ops):
    # right-to-left collapse
    a, b, c, d = seq
    op1, op2, op3 = ops

    try:
        return op1(a, op2(b, op3(c, d)))
    except ZeroDivisionError:
        return -1

def apply_ops_lr(seq, ops):
    # left-ro-right collapse
    a, b, c, d = seq
    op1, op2, op3 = ops

    try:
        return op1(op2(op3(a, b), c), d)
    except ZeroDivisionError:
        return -1


add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

def str_op(op):
    # printing helper for ops
    if op == add: return '+'
    elif op == sub: return '-'
    elif op == mul: return '*'
    elif op == div: return '/'

def count(nums):
    if not nums or nums[0] != 1:
        return 0
    
    # count how long the sequence 1, 2, ...
    i = 0
    while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
        i += 1
        
    return i + 1
    
def arithmetic_expressions():
    number_sets = []
    for a in range(1, 7):
        for b in range(a+1, 8):
            for c in range(b+1, 9):
                for d in range(c+1, 10):
                    number_sets.append([a, b, c, d])

    op_seqs = []
    for op1 in [add, sub, mul, div]:
        for op2 in [add, sub, mul, div]:
            for op3 in [add, sub, mul, div]:
                op_seqs.append([op1, op2, op3])

    ans = ''
    longest_seq = float('-inf')
    for nums in number_sets:
        seen = set()
        seqs = permutations(nums)
        for seq in seqs:
            for op_seq in op_seqs:
                for apply_ops in [apply_ops_lr, apply_ops_rl]:
                    res = apply_ops(seq, op_seq)
                    if res >= 1 and int(res) == res:
                        seen.add(int(res))
                    
        srt = sorted(list(seen))
        cnt = count(srt)
        old = longest_seq
        longest_seq = max(longest_seq, cnt)
        if longest_seq > old:
            ans = nums
        print(f"cnt: {cnt}, seq: {nums} -- {srt}")

    return ans, longest_seq
                
if __name__ == "__main__":
    ans, cnt = arithmetic_expressions()
    a, b, c, d = ans
    print(
        f"Nums {a} < {b} < {c} < {d} generates longest 1--n seq: {cnt}"
    )
