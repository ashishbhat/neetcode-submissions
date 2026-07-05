class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g: dict[int, list[int]] = collections.defaultdict(list)
        indegree: dict[int, int] = {i: 0 for i in range(numCourses)}

        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1
        
        queue = collections.deque([k for k,v in indegree.items() if v == 0])
        completed = []

        while queue:
            course = queue.popleft()
            completed.append(course)

            for nei in g[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if len(completed) == numCourses:
            return completed
        else:
            return []