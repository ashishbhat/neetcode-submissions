class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curr = intervals[0]
        for nxt in intervals[1:]:
            if nxt[0] <= curr[1]:
                curr[0] = min(curr[0], nxt[0])
                curr[1] = max(curr[1], nxt[1])
            else:
                res.append(curr)
                curr = nxt
        res.append(curr)
        return res