import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        # We only need the counts; the task name doesn't matter for the result
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        cooldown = deque() # stores (neg_count, available_time)
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                # Process the most frequent task
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    cooldown.append((count, time + n))
            
            # Check if any task is finished with cooldown
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])
            
            # Optimization: If no tasks are ready, skip time to the next available task
            if not max_heap and cooldown:
                time = cooldown[0][1] - 1 # -1 because time increments at start of loop
                
        return time