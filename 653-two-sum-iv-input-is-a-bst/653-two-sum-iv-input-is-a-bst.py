# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        seen = set()
        def dfs(root,seen, target):
            if root is None:
                return False
            if (target-root.val) in seen:
                return True
            seen.add(root.val)
            return dfs(root.left,seen,target) or dfs(root.right, seen, target)
        
        return dfs(root,seen,target)