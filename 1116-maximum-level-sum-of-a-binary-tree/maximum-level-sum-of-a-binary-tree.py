# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        max_sum = root.val
        min_lvl = 1

        cur_lvl = 0
        while queue:
            cur_lvl += 1
            lvl_sum = 0
            lvl_width = len(queue)
            for i in range(lvl_width):
                cur = queue.popleft()
                lvl_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if lvl_sum > max_sum:
                max_sum = lvl_sum
                min_lvl = cur_lvl
            
        return min_lvl
            