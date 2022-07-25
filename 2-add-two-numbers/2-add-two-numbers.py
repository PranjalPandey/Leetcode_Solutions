# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        pre = None
        head = None
        while curr1 or curr2:
            value = carry
            if curr1:
                value+=curr1.val
                curr1=curr1.next
            if curr2:
                value+=curr2.val
                curr2=curr2.next
            
            carry = value//10
            value = value%10
            
            node = ListNode(value)
            if pre:
                pre.next = node
                pre = pre.next
            else:
                head = node
                pre = node
        if carry:
            pre.next = ListNode(carry)
        return head