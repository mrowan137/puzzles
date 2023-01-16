"""
Runtime: 301 ms, faster than 61.26% of Python3 online submissions for Accounts Merge.
Memory Usage: 20.7 MB, less than 34.63% of Python3 online submissions for Accounts Merge.
"""
from collections import defaultdict


class Solution:
    def dfs(self, graph, node, visited, connected):
        if node in visited:
            return
        visited.add(node)
        connected.append(node)
        for neighbor in graph[node]:
            self.dfs(graph, neighbor, visited, connected)
        return

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # make adjacency list
        graph = defaultdict(set)
        email_to_name = {}
        for a in accounts:
            name, emails = a[0], a[1:]
            for e in emails:
                graph[emails[0]].add(e)
                graph[e].add(emails[0])
                email_to_name[e] = name

        # do DFS on adjacency list to find connected components
        visited = set()
        res = []
        for node in graph:
            connected = []
            for neighbor in graph[node]:
                self.dfs(graph, neighbor, visited, connected)
            if connected:
                res.append([email_to_name[node]] + sorted(connected))

        return res
