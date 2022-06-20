# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, head):
        pre = None
        curr = head
        nextt = None
        while curr:
            nextt = curr.next
            curr.next = pre
            pre = curr
            curr = nextt
        return pre
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.rev(slow)
        while mid:
            if curr.val != mid.val:
                return False
            curr = curr.next
            mid = mid.next
        return True