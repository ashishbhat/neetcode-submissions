import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x - y != 0:
                heapq.heappush(heap,-abs(x-y))
        
        return 0 if not heap else  -heap[0]