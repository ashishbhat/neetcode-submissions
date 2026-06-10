"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque()
        visited = set()
        clone_map = {}
        clone = Node(node.val, node.neighbors)
        clone_map[node] = clone
        queue.append(clone)
        visited.add(node)

        while queue:
            node = queue.pop()

            neighbors = []
            for neighbor in node.neighbors:
                cloned_neighbor = None
                if neighbor in clone_map:
                    cloned_neighbor = clone_map[neighbor]
                else:
                    cloned_neighbor = Node(neighbor.val, neighbor.neighbors)
                    clone_map[neighbor] = cloned_neighbor
                neighbors.append(cloned_neighbor)
                if not neighbor in visited:
                    queue.append(cloned_neighbor)
                    visited.add(neighbor)
            node.neighbors = neighbors
        return clone