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
        
        n1 = self.getSize(l1)
        n2 = self.getSize(l2)

        if n1 < n2:
            l2, l1 = l1, l2
            n2, n1 = n1, n2
        l1_head = l1
        l2_head = l2
        
        summ = carry = 0
        while l1 != None and l2 != None:
            summ = l1.val + l2.val + carry
            l1.val = summ % 10
            carry = summ // 10
                        
            if l1.next == l2.next == None:
                if carry:
                        l1.next = ListNode(1)
                return l1_head
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            total = l1.val + carry
            l1.val = total % 10
            carry = total // 10
            if l1.next == None:
                if carry:
                    l1.next = ListNode(1)
                break;
            l1 = l1.next


        return l1_head




