# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getSize(self, head: Optional[ListNode]) -> int:
        n = 0
        while head:
            n += 1
            head = head.next
        return n

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if self.getSize(l1) < self.getSize(l2):
            l2, l1 = l1, l2
        l1_head = l1
        l2_head = l2
        
        summ = carry = 0
        prev = None
        while l1 or l2:
            summ = l1.val + (l2.val if l2 else 0) + carry
            l1.val = summ % 10
            carry = summ // 10
            prev = l1
            l1 = l1.next
            l2 = l2.next if l2 else l2
        if carry:
            prev.next = ListNode(1)
        return l1_head




