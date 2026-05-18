#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def length(self, head:Optional[ListNode]) -> int:
        n = 0
        while head:
            n += 1
            head = head.next
        return n
    def reverse(self, head, k):
        prev = None
        current = head
        next = None
        for _ in range(k):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head.next = current
        return prev, head, next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = ListNode()
        s = p
        while self.length(head) >= k:
            head, tail, next = self.reverse(head, k)
            p.next = head
            p = tail
            head = next
        return s.next