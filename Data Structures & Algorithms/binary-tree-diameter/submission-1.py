# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root):
            nonlocal result
            if not root:
                return 0
            

            leftDiam = dfs(root.left)
            rightDiam = dfs(root.right)
            result = max(result, leftDiam + rightDiam)
            return 1 + max(leftDiam, rightDiam)
        
        dfs(root)
        return result
        
