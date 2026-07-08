class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i, v in enumerate(tickets):
            queue.append([i, v])

        ticker = 0
        while True:
            ticker += 1
            front = queue.popleft()
            front[1] -= 1
            if front[1] == 0 and front[0] == k:
                return ticker
            elif front[1] != 0:
                queue.append(front)
        