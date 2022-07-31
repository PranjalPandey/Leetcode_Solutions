# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        l = head
        count = 0
        while l:
            l = l.next
            count +=1
        l = head
        pre = None
        # print(count)
        k = k%count
        rem = count-k
        if k ==0: return head
        # print(rem)
        while rem:
            pre = l
            l = l.next
            rem-=1
        pre.next = None
        h2 = l
        while l.next:
            l = l.next
        l.next = head
        head = h2
        return head