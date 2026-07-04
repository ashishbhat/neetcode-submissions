class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(set)
        trusts = set()

        for i, j in trust:
            trusted[j].add(i)
            trusts.add(i)

        for i in range(1, n+1):
            if i not in trusts:
                if len(trusted[i]) == n - 1 and i not in trusted[i]:
                    return i
        return -1