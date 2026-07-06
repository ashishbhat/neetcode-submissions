class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {v:[] for v in range(n)}
        connected = 0
        visited = set()
        
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u) -> None:
            visited.add(u)
            for v in g[u]:
                if v not in visited:
                    dfs(v)

        for u in g.keys():
            if u not in visited:
                connected += 1
                dfs(u)

        return connected