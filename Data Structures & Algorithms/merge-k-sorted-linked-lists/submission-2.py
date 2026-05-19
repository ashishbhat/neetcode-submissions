# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = [(x.val, i, x) for i,x in enumerate(lists) if x]
        heapq.heapify(heads)
        result: ListNode = ListNode()
        temp: ListNode = result

        while heads:
            min_val, list_id, min_node = heapq.heappop(heads)
            temp.next = min_node
            temp = temp.next
            if min_node.next:
                heapq.heappush(heads, (min_node.next.val, list_id, min_node.next))
        return result.next
