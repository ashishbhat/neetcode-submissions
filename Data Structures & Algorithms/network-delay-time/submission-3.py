from dataclasses import dataclass
import heapq

@dataclass
class Edge:
    to: int = -1
    weight: int = -1

@dataclass
class Node:
    time: int
    n: int

    def __lt__(self, other):
        if isinstance(other,Node):
            return self.time < other.time
        return False

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        time = {i:float('inf') for i in range(1,n+1)}
        time[k] = 0
        g: dict[int, List[Edge]] = {i:[] for i in range(1,n+1)}

        for u, v, t in times:
            g[u].append(Edge(v,t))
        print(g)

        heap = []
        heapq.heappush(heap, Node(0, k))

        while heap:
            fromm = heapq.heappop(heap)
            if fromm.n in visited:
                continue
            visited.add(fromm.n)

            for edge in g[fromm.n]:
                to = edge.to
                if fromm.time + edge.weight < time[to]:
                    time[to] = fromm.time + edge.weight
                    heapq.heappush(heap, Node(time[to], to))
        
        print(time)
        res = max(time.values())
        return -1 if res == float('inf') else res



