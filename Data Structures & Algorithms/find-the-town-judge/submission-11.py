class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        notTrusts = {i for i in range(1, n+1)}

        for i, j in trust:
            trusted[j] += 1
            notTrusts.discard(i)

        for i in notTrusts:
            if trusted[i] == n - 1:
                return i
        return -1