import heapq
class Solution:
    def dist(self, x: int, y: int) -> int:
        return x**2 + y**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-self.dist(x,y), x, y) for x,y in points[:k]]
        heapq.heapify(heap)

        for x, y in points[k:]:
            if - self.dist(x, y) > heap[0][0]:
                heapq.heapreplace(heap, (- self.dist(x,y), x, y))
            
        return [[x,y] for _,x,y in heap]
