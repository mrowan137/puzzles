"""
Runtime: 32 ms, faster than 79.50% of Python3 online submissions for Alien Dictionary.
Memory Usage: 14.4 MB, less than 22.74% of Python3 online submissions for Alien Dictionary.
"""
# O(total length of all words summed together); get this in a case like
# [abcdef, abcdefg, abcdefgh, ...] (variation in the last letter)
from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Initialize datastructures to make adjacency list
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        # Loop over pairs of words to fill adjacency list
        for w1, w2 in zip(words, words[1:]):
            # edge case: make sure second not a prefix of first
            if w1 != w2 and w1.find(w2) == 0:
                return ""

            for l1, l2 in zip(w1, w2):
                # Look only for the first difference between words
                # Differences beyond do not matter (abacus, algorithm)
                if l1 != l2:
                    if l2 not in adj[l1]:
                        adj[l1].add(l2)
                        in_degree[l2] += 1
                    break

        # Pick off nodes with indegree of 0
        output = []
        queue = [c for c in in_degree if in_degree[c] == 0]
        print(in_degree)
        while queue:
            c = queue.pop(0)
            output.append(c)
            for d in adj[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # if we did not use all letters in the output, found a cycle
        if len(output) < len(in_degree):
            return ""

        return "".join(output)


from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Initialize datastructures to make adjacency list
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        # Loop over pairs of words to fill adjacency list
        for w1, w2 in zip(words, words[1:]):
            # edge case: make sure second not a prefix of first
            if w1 != w2 and w1.find(w2) == 0:
                return ""

            for l1, l2 in zip(w1, w2):
                # Look only for the first difference between words
                # Differences beyond do not matter (abacus, algorithm)
                if l1 != l2:
                    if l2 not in adj[l1]:
                        adj[l1].add(l2)
                        in_degree[l2] += 1
                    break

        # Pick off nodes with indegree of 0
        output = []
        queue = [c for c in in_degree if in_degree[c] == 0]
        print(in_degree)
        while queue:
            c = queue.pop(0)
            output.append(c)
            for d in adj[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # if we did not use all letters in the output, found a cycle
        if len(output) < len(in_degree):
            return ""

        return "".join(output)
