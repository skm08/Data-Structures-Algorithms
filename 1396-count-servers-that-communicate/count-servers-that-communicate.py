class Solution:
    def countServers(self, g: List[List[int]]) -> int:
        return (p:=[*map(sum,g)],q:=[*map(sum,zip(*g))]) and sum(p[i]+q[j]>2 for i,r in enumerate(g) for j,v in enumerate(r) if v)