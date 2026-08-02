class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = float('-inf')
        res = 0

        for i in range(len(intervals)):
            if intervals[i][0] < prevEnd:
                res += 1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
        return res