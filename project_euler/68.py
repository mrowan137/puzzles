"""
Q: Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set:
  4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form
16- and 17-digit strings. What is the maximum 16-digit string for a "magic"
5-gon ring?

A: 6531031914842725
"""
import itertools


def encode(fivegon):
    # take fivegon from 1x10 representation to 5x3;
    # this is small number of vertices to handle, we can do manual
    # [1 2 3 4 5 6 7 8 9 10] --> [ [ 1 2 3],
    #                              [ 4 3 5],
    #                              [ 6 5 7],
    #                              [ 8 7 9],
    #                              [10 9 2] ]
    nonunique_encoded_fivegon = [
        [fivegon[0], fivegon[1], fivegon[2]],
        [fivegon[3], fivegon[2], fivegon[4]],
        [fivegon[5], fivegon[4], fivegon[6]],
        [fivegon[7], fivegon[6], fivegon[8]],
        [fivegon[9], fivegon[8], fivegon[1]],
    ]

    # fivegon is described uniquely by starting at lowest-value external node
    outer_nodes = [group[0] for group in nonunique_encoded_fivegon]
    smallest_outer_node = min(outer_nodes)
    roll_to_index = outer_nodes.index(smallest_outer_node)

    # roll around to the smallest external node, giving the unique encoding
    encoded_fivegon = (
        nonunique_encoded_fivegon[roll_to_index:]
        + nonunique_encoded_fivegon[:roll_to_index]
    )

    return encoded_fivegon


def is_magic_fivegon(encoded_fivegon):
    # fivegon is the encoded 5x3 array of numbers
    s0 = sum(encoded_fivegon[0])
    return all(s0 == s for s in map(sum, encoded_fivegon))


def magic_fivegon_rings():
    # 1. generate all 10! ~ 3^6 encodings that might be a magic fivegon
    maybe_magic_fivegon_rings = list(itertools.permutations(range(1, 11)))

    # 2. encode the fivegon in 1x10 --> 5x3 representation
    maybe_magic_fivegon_rings_encoded = [
        encode(mfr) for mfr in maybe_magic_fivegon_rings
    ]

    # 3.
    magic_fivegon_rings_encoded = []
    for mfr in maybe_magic_fivegon_rings_encoded:
        if is_magic_fivegon(mfr):
            magic_fivegon_rings_encoded.append(mfr)

    return magic_fivegon_rings_encoded


def answer():
    res = float("-inf")
    mfrs = magic_fivegon_rings()
    for mfr in mfrs:
        s = "".join("".join(str(d) for d in group) for group in mfr)

        # consider just the 16-length fivegon
        if len(s) != 16:
            continue

        res = max(res, int(s))

    return res


if __name__ == "__main__":
    print(f"Greatest length-16 magic fivegon ring: {answer()}")
