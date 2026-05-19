from collections import deque
from typing import Optional
class LRUCache:
    class Node:
        def __init__(self,
                    key: int,
                    val: int,
                    nxt: Optional[LRUCache.Node] = None,
                    prev: Optional[LRUCache.Node] = None):
            self.key = key
            self.val = val
            self.nxt = nxt
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity: int  = capacity
        self.node_map: dict[int, LRUCache.Node] = {}
        self.size: int  = 0
        self.head: LRUCache.Node = None
        self.tail: LRUCache.Node = None

    def get(self, key: int) -> int:
        print(f'get = {key}')
        node = self.node_map.get(key, None)
        if not node: return -1
        self.__remove_node(node)
        self.__move_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        print(f'put = {key},{value}')   
        if key in self.node_map:
            tmp = self.node_map[key]
            self.__remove_node(tmp)
            self.size -= 1
            tmp.val = value
            self.__move_to_end(tmp)    
            self.size += 1
            return      
        if self.size == self.capacity:
            self.__remove_node(self.head)
            self.size -= 1
        self.__move_to_end(LRUCache.Node(key, value))
        self.size += 1

    def __move_to_end(self, node: LRUCache.Node):
        if self.tail == None and  self.head == None:
            self.tail = node 
            self.head = node
            self.node_map[node.key] = node
        else:
            self.tail.nxt = node
            self.tail.nxt.prev = self.tail
            self.tail = self.tail.nxt
            self.node_map[node.key] = self.tail

    def __remove_node(self, node: Node):
        if self.head == node and self.tail == node:
            self.tail = self.head = None
        elif node is self.head:
            self.head = self.head.nxt
            self.head.prev.nxt = None
            self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.nxt.prev = None
            self.tail.nxt = None
        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            node.nxt = None
            node.prev = None
        del self.node_map[node.key]






