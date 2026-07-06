class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            else:
                return False
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set()
        visited.add(edges[0][0])

        def dfs(node, parent) -> bool:
            result = True
            for nei in g[node]:
                if nei not in visited:
                    visited.add(nei)
                    result &= dfs(nei, node)
                elif nei != parent:
                    result =  False
            return result


        return dfs(edges[0][0], -1) and len(visited) == n