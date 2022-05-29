# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if head is None: 
            return None
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow