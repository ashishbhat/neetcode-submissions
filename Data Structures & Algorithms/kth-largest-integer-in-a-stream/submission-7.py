import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [ x for x in nums[:k]]
        heapq.heapify(self.heap)
        if k < len(nums):
            for i in nums[k:]:
                if i > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, i)

    def add(self, val: int) -> int:
        print(self.heap)
        if not self.heap or len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
