class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g: dict[int, list[int]] = collections.defaultdict(list)
        indegree: dict[int, int] = {i: 0 for i in range(numCourses)}

        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1
        
        queue = collections.deque([k for k,v in indegree.items() if v == 0])
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for nei in g[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return completed == numCourses