"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map  = defaultdict(Node)
        deep_copy = Node(0)
        temp = head
        temp2 = deep_copy
        while temp != None:
            new_node = Node(temp.val)
            node_map[temp] = new_node
            temp2.next = new_node
            temp = temp.next
            temp2 = temp2.next
        
        temp = head
        temp2 = deep_copy.next
        while temp != None:
            temp2.random = node_map.get(temp.random, None)
            temp = temp.next
            temp2 = temp2.next
        return deep_copy.next

