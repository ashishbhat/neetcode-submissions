import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      freq = Counter(tasks)

      # Max-heap using negative counts
      max_heap = [-count for count in freq.values()]
      heapq.heapify(max_heap)

      cooldown = deque()
      time = 0

      while max_heap or cooldown:
          time += 1

          # First, bring back all tasks whose cooldown has expired.
          while cooldown and cooldown[0][0] <= time:
              available_time, count = cooldown.popleft()
              heapq.heappush(max_heap, count)

          # Then run one available task this cycle.
          if max_heap:
              count = heapq.heappop(max_heap)
              count += 1  # reduce remaining count because it is negative

              if count != 0:
                  available_time = time + n + 1
                  cooldown.append((available_time, count))

      return time

                            



        