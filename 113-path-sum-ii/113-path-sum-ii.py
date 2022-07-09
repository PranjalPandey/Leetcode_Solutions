# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcPathSum(self, root, targetSum, buffer, output):
        if root:
            if not root.left and not root.right and targetSum==root.val:
                buffer+=[root.val]
                output.append(buffer.copy())
                return
            self.calcPathSum(root.left, targetSum - root.val, buffer+[root.val], output)
            self.calcPathSum(root.right, targetSum - root.val, buffer+[root.val], output)
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        self.calcPathSum(root,targetSum, [], output)
        return output

        
            
        