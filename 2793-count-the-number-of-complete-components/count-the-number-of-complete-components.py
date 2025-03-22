class Solution:
    def dfs(self, curr, nodes, edges, adj, visited):
        nodes[0] += 1
        visited[curr] = True
        for nbr in adj[curr]:
            edges[0] += 1
            if not visited[nbr]:
                self.dfs(nbr, nodes, edges, adj, visited)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        complete_components = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                nodes = [0]
                edges_count = [0]
                self.dfs(i, nodes, edges_count, adj, visited)
                if edges_count[0] == nodes[0] * (nodes[0] - 1):
                    complete_components += 1
        return complete_components