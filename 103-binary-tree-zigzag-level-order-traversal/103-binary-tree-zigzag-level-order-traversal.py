# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d="r"
        if root==None:
            return []
        level = [root]
        next_level = []
        ans = [[root.val]]
        while level:
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                if d=="r":
                    ans.append([r.val for r in reversed(next_level)])
                else:
                    ans.append([r.val for r in next_level])
                    
            d="r" if d=="l"else "l"
            level = next_level.copy()
            next_level = []
        return ans
                
                        