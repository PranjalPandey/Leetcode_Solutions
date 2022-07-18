# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
     
        if root==None:
            return 0
        count=0
        def calculateNodes(root,count):
            
            if root:
                count+=1
            if root.left:
                count = calculateNodes(root.left,count)
            if root.right:
                count = calculateNodes(root.right,count)
            return count
        return calculateNodes(root,count)
        
        