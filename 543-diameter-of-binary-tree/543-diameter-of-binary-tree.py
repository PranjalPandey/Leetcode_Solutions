# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameter(self,root):
        if root is None:
            return 0,0
        lh,ld= self.diameter(root.left)
        rh,rd = self.diameter(root.right)
        
        h = max(lh,rh)+1
        d = max(ld,rd,lh+rh)
        return h,d
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.diameter(root)[1]