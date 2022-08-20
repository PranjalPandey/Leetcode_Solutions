# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def distribute(root):
            nonlocal res
            if root is None:
                return 0
            l_c =  distribute(root.left)
            r_c = distribute(root.right)
            res +=abs(l_c)+abs(r_c)
            return root.val+l_c+r_c-1
        distribute(root)
        return res                     
        