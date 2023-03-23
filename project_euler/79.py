"""
Q: A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278, they
may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.

A: 73162890
"""


def passcode_derivation(file_name):
    # interpret this as a topological sort question;
    # build the DAG, add the 0-dependency digits
    # to the passcode, update the dependency counter,
    # iterate; this will produce the shortest passcode

    # read file
    clues = []
    with open(file_name) as f:
        for line in f:
            clues.append(line.replace("\n", ""))

    # all the numbers that appear in
    # the clues (vertices of the DAG)
    vertices = set()
    for c in "".join(clues):
        vertices.add(c)

    # construct DAG
    graph = {v: set() for v in vertices}
    for clue in clues:
        for i, c in enumerate(clue):
            for j in range(i + 1, len(clue)):
                graph[c].add(clue[j])

    # topological sorting
    in_degree = {v: 0 for v in vertices}
    for neighbors in graph.values():
        for v in neighbors:
            in_degree[v] += 1

    # construct the passcode, adding those
    # digits with zero dependencies
    passcode = ""
    queue = [v for v in in_degree if in_degree[v] == 0]
    while queue:
        no_dependency = queue.pop(0)
        passcode += no_dependency
        for v in graph[no_dependency]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return passcode


if __name__ == "__main__":
    f = "./keylog.txt"
    print(
        "Shortest passcode consistent with {}: {}".format(
            f, passcode_derivation(f)
        )
    )
