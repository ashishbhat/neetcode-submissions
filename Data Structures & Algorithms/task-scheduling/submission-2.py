import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        cooldown = deque()
        cycle = 0

        while max_heap or cooldown:
            cycle += 1
            while cooldown and cooldown[0][0] <= cycle:
                available_time, count = cooldown.popleft()
                heapq.heappush(max_heap, count)
            
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count != 0:
                    cooldown.append((cycle+n+1, count))
        return cycle

                            



        