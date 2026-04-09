class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        INF = 1 << 25

        # Map characters to indices
        charmap = {chr(ord('a') + i): i for i in range(26)}

        # Distance matrix
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        # Direct transformations
        for u, v, c in zip(original, changed, cost):
            ui = charmap[u]
            vi = charmap[v]
            if c < dist[ui][vi]:
                dist[ui][vi] = c

        # Floyd–Warshall
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                dik = dist[i][k]
                if dik >= INF:
                    continue
                di = dist[i]
                for j in range(26):
                    nd = dik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        # Compute total cost
        total = 0
        for x, y in zip(source, target):
            xi = charmap[x]
            yi = charmap[y]
            if dist[xi][yi] >= INF:
                return -1
            total += dist[xi][yi]

        return total