"""
Q: A natural number, N, that can be written as the sum and product of a given
set of at least two natural numbers, {a1, a2, ..., ak} is called a product-sum
number: N = a1 + a2 + ... + ak = a1 * a2 * ... * ak.

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a
minimal product-sum number. The minimal product-sum numbers for sets of size,
k = 2, 3, 4, 5, and 6 are as follows.

  k = 2: 4 = 2 * 2 = 2 + 2
  k = 3: 6 = 1 * 2 * 3 = 1 + 2 + 3
  k = 4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
  k = 5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
  k = 6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is
4 + 6 + 8 + 12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

A: 7587457
"""

from math import prod
from collections import defaultdict


def primes_less_than(n):
    # return primes less than n
    nums = list(range(2, n))

    for i, num in enumerate(nums):
        if num == -1:
            continue

        j = i
        while True:
            j += num

            if j >= len(nums):
                break

            nums[j] = -1

    return [m for m in nums if m != -1]


def compute_prime_factorization(n, primes):
    pf = []
    for p in primes:
        if n == 1:
            break

        while n % p == 0:
            pf.append(p)
            n /= p

    return pf


def subtract_sequences(a, b):
    # return the seq a - b
    # assumptions:
    #   - a is longer than b
    #   - a and b are in sorted order
    #   - a contains b
    if len(a) < len(b):
        return []

    i, j = 0, 0  # pointers into a, b
    c = []  # the sequence a - b

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1
        else:
            c.append(a[i])

        i += 1

    if i < len(a):
        c += a[i:]

    return c if j == len(b) else []


def mps(lo, hi):
    # more optimized than `mps_brute_force` below, but still takes awhile
    factor = 2
    primes = primes_less_than(hi * factor + 1)
    prime_factorize = {}
    for n in range(2, hi * factor + 1):
        print(f"computing prime factorization: {n}")
        prime_factorize[n] = compute_prime_factorization(n, primes)

    k_to_ps_seq = defaultdict(lambda: [])
    k_to_ps_min = defaultdict(lambda: float("inf"))
    seen = set()

    for k in range(lo, factor * hi + 1):
        # whether this upper bound is big enough needs to be proved;
        # for now it is a conjecture based on observations and experiments
        print(f" ********** k = {k}/{int(factor*hi)} ********** ")
        seq = prime_factorize[k]
        to_explore = [seq] if seq and seq[-1] != k else []
        while to_explore:
            curr = to_explore.pop()

            # record the ps if it's smaller than
            # anything seen so far for given k
            s, l = prod(curr), len(curr) + (prod(curr) - sum(curr))

            prev = k_to_ps_min[l]
            k_to_ps_min[l] = min(s, k_to_ps_min[l])
            if k_to_ps_min[l] <= prev and prod(seq) >= sum(seq):
                while k_to_ps_seq[l] and prod(k_to_ps_seq[l][0]) > s:
                    k_to_ps_seq[l].pop(0)

                k_to_ps_seq[l].append(curr)

            # generate other possible ps sequences
            for k_ in sorted(k_to_ps_seq):
                for ps_seq in k_to_ps_seq[k_]:
                    ps_val = prod(ps_seq)
                    if ps_val < k_to_ps_min[l] and s % ps_val == 0:
                        # 1. compute curr - ps_seq
                        # 2. add the ps_val, sort it
                        # 3. seq goes into the new one
                        maybe_new_seq = subtract_sequences(curr, ps_seq) + [
                            ps_val
                        ]
                        if maybe_new_seq and not tuple(maybe_new_seq) in seen:
                            seen.add(tuple(maybe_new_seq))
                            to_explore.append(maybe_new_seq)

    res, seen = 0, set()
    for k, ps in sorted(k_to_ps_min.items()):
        if k <= hi and not ps in seen:
            res += ps

        seen.add(ps)

    return res


def find_product_sum_sequences(k):
    # find product-sum sequences of length k
    seqs = []

    # explore: sequences that may lead to valid ps sequence
    to_explore, seen = [[]], set()

    while to_explore:
        seq = to_explore.pop()

        if tuple(seq) in seen:
            continue

        seen.add(tuple(seq))

        if seq and seq[0] > 2:
            continue

        if len(seq) > k:
            # the sequence got too long
            continue

        if len(seq) == k and sum(seq) == prod(seq):
            # found a valid sequence
            seqs.append(seq)
            continue

        if 1 < len(seq) < k and sum(seq) <= prod(seq):
            # product is already too big, adding more of seq[-1] (i.e., the
            # smallest possibility since we encode in sorted order) will result
            # in a sequence with product != sum
            continue

        # keep filling out the sequence
        for i in range(seq[-1] if seq else 1, k + 1):
            proposed_seq = seq + [i]
            to_explore.append(proposed_seq)

    return seqs


def mps_brute_force(lo, hi):
    # this function is a useful check of more optimized calculation above.
    # find the minimal product-sum of length k:
    #   1. find all product-sum of length k
    #   2. take the smallest one
    #
    # observe for sequence of length k, an upper bound for the product is k
    # e.g. 1 * 1 * ... * k < 1 + 1 + ... k

    # a list of all product-sum sequences
    ps_sequences = set()

    # for each possible product target, generate & record valid product-sum seqs
    for _, target in enumerate(range(lo, hi + 1)):
        seqs = find_product_sum_sequences(target)
        minimal = min(sum(s) for s in seqs)
        print(
            f"k = {target} has minimal {minimal} : {[s for s in seqs if sum(s) == minimal]}"
        )
        if minimal not in ps_sequences:
            ps_sequences.add(minimal)
            print(f"for k = {target} adds ps = {minimal}")

    print(f"The set of minimal product-sum numbers: {list(ps_sequences)}")
    return sum(ps for ps in ps_sequences)


if __name__ == "__main__":
    K = 12000
    print(
        # f"Sum of minimal product-sum numbers for 2 <= k <= {K}: "
        # f"{mps_brute_force(2, K)} [brute force]\n"
        f"Sum of minimal product-sum numbers for 2 <= k <= {K}: {mps(2, K)}"
    )
