# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inord = []
        def inorder(root,inord):
            # Nonlocal inord
            if root is None:
                return
            inorder(root.left,inord)
            inord.append(root.val)
            inorder(root.right, inord)
        inorder(root, inord)
        left = 0 
        right = len(inord)-1
        # print(inord)
        def make_bst(left,right,inord):
            if left>right:
                return None
            mid = (right+left)//2
            left = make_bst(left,mid-1,inord)
            right = make_bst(mid+1, right,inord)
            root = TreeNode(val = inord[mid], left = left, right = right)
            return root
        return make_bst(left,right,inord)