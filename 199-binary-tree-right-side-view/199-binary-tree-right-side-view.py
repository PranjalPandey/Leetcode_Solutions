# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        curr_level = deque()
        curr_level.append(root)
        output = []
        while curr_level:
            output.append(curr_level[-1].val)
            size = len(curr_level)
            for i in range(size):
                node = curr_level[0]
                curr_level.popleft()
                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)
                
                
        
        return output