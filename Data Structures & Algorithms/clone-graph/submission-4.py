"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        mapping: dict[Node, Node] = collections.defaultdict(Node)
        copy = Node(node.val, None)
        mapping[node] = copy
        queue = collections.deque([node])

        while queue:
            original = queue.popleft()
            cloned = mapping[original]

            for neighbour in original.neighbors:
                if neighbour not in mapping:
                    cloned_neighbour = Node(neighbour.val, None)
                    mapping[neighbour] = cloned_neighbour
                    cloned.neighbors.append(cloned_neighbour)
                    queue.append(neighbour)
                else:
                    cloned.neighbors.append(mapping[neighbour])
        return copy


