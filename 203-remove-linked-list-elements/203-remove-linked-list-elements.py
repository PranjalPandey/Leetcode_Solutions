# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        if head is None:
            return None
        pre = None
        while curr:
            if curr.val==val and pre:
                pre.next = curr.next
                
            elif curr.val==val and not pre:
                head = curr.next
            else:
                pre = curr
            curr = curr.next
        return head