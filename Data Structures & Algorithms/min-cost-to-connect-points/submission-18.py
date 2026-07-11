class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 0
        points = {i : point for i, point in enumerate(points)}
        # graph with n*n edges
        g = defaultdict(list)
        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                g[i].append((j, dist))
                g[j].append((i, dist))

        visited = set()
        distances = [float('inf')] * n
        heap = []
        heapq.heappush(heap, (0, 0))

        while heap:
            s, u = heapq.heappop(heap)
            if u in visited:
                continue
            ans += s
            visited.add(u)
            if len(visited) == n:
                break

            for v, s in g[u]:
                if distances[v] > s:
                    distances[v] = s
                    heapq.heappush(heap, (s, v))
        return ans

        

        