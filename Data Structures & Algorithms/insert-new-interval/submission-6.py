class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = []
        curr = intervals[0]
        for nxt in intervals[1:]:
            if nxt[0] <= curr[1]:
                curr[0] = min(curr[0], nxt[0])
                curr[1] = max(curr[1], nxt[1])
            else:
                result.append(curr)
                curr = nxt
        result.append(curr)
        return result



