# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        levels = []
        MOD = 10**9 + 7
        def dfs(root):
            nonlocal total_sum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            val = root.val + left + right
            levels.append(val)
            total_sum+= root.val
            return val
        dfs(root)
        result = 0
        for i in levels:
            value = total_sum - i
            if (value * i) > result:
                result = value*i 
        return result % MOD