import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        #create a max heap of task based on count
        heap = [(-count, task, 0) for task, count in freq.items()]
        heapq.heapify(heap)

        cooldown = deque()
        cycle = 0

        while cooldown or heap:
            cycle += 1

            while cooldown and cooldown[0][2] <= cycle:
                task = cooldown.popleft()
                heapq.heappush(heap, task)

            if heap:
                count, name, _ =  heapq.heappop(heap)
                count += 1

                if count != 0:
                    cooldown.append((count, name, cycle + n + 1))

        return cycle