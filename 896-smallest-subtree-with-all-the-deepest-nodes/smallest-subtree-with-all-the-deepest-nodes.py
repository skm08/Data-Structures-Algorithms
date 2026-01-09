# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, d):
            depths[node] = d
            if node.left:
                edges[node.left] = node
                dfs(node.left, d + 1)
            if node.right:
                edges[node.right] = node
                dfs(node.right, d + 1)
            
        
        edges = {}
        depths = {}
        dfs(root, 1)
        visited = set()
        queue = deque([node for node, d in depths.items() if d == max(depths.values())])
        
        while queue:
            if len(queue) == 1:
                return queue[0]
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in edges and edges[node] not in visited:
                    queue.append(edges[node])
                    visited.add(edges[node])
    