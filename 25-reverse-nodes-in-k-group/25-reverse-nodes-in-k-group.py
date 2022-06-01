# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        count = 0
        curr = head
        nextt = None
        pre = None
        while curr is not None and count<k:
            nextt = curr.next
            curr.next = pre
            pre = curr
            curr = nextt
            count+=1
            
        if count!=k:
            curr=pre
            pre=None
            nextt=None
            while curr is not None :
                nextt = curr.next
                curr.next = pre
                pre = curr
                curr = nextt
            
            
        if nextt is not None:
            head.next = self.reverseKGroup(nextt,k)
        return pre
        