class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        subtree_xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = [0]

        # Step 1: DFS to fill in_time, out_time, subtree XOR
        def dfs(node, par):
            parent[node] = par
            in_time[node] = time[0]
            time[0] += 1
            xor_val = nums[node]
            for nei in graph[node]:
                if nei != par:
                    xor_val ^= dfs(nei, node)
            out_time[node] = time[0]
            subtree_xor[node] = xor_val
            return xor_val

        total_xor = dfs(0, -1)

        # Step 2: get edge list
        edge_list = []
        for u in range(1, n):
            edge_list.append((parent[u], u))

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        min_score = float('inf')

        # Step 3: try all edge pairs (n ≤ 10^4 so ~50M loops is okay now)
        for i in range(len(edge_list)):
            for j in range(i+1, len(edge_list)):
                _, u = edge_list[i]
                _, v = edge_list[j]

                if is_ancestor(u, v):
                    a = subtree_xor[v]
                    b = subtree_xor[u] ^ subtree_xor[v]
                    c = total_xor ^ subtree_xor[u]
                elif is_ancestor(v, u):
                    a = subtree_xor[u]
                    b = subtree_xor[v] ^ subtree_xor[u]
                    c = total_xor ^ subtree_xor[v]
                else:
                    a = subtree_xor[u]
                    b = subtree_xor[v]
                    c = total_xor ^ a ^ b

                min_score = min(min_score, max(a, b, c) - min(a, b, c))

        return min_score