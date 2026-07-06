class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        if len(edges) != n-1:
            return False

        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set()
        visited.add(edges[0][0])

        def dfs(node, parent) -> bool:
            for nei in g[node]:
                if nei not in visited:
                    visited.add(nei)
                    if not dfs(nei, node):
                        return False
                elif nei != parent:
                    return False
            return True


        return dfs(edges[0][0], -1) and len(visited) == n