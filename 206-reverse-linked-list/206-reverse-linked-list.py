# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        nextt = None
        curr = head
        if curr is None:
            return None 
        
        while curr:
            nextt = curr.next
            curr.next = pre
            pre = curr
            curr = nextt
        return pre
            
        