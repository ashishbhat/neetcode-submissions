class DSU:
    def __init__(self, n: int) -> None:
        self.root = {i:i for i in range(1, n+1)}
        self.sz = {i:1 for i in range(1,n+1)}
        self.components = n

    def find(self, a: int):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def isConnected(self, a: int, b: int):
        return self.find(a) == self.find(b)
    
    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        
        if self.sz[ra] > self.sz[rb]:
            rb, ra = ra, rb
        
        self.root[ra] = rb
        self.sz[rb] += self.sz[ra]
        self.components -= 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        result = []

        for u, v in edges:
            if not dsu.union(u, v):
                result = [u, v]
        return result

        



        