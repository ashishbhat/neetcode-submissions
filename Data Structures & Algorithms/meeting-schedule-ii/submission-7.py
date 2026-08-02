"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x.start)
        heap = [(intervals[0].end, intervals[0].start)]
        minRooms = 1

        for interval in intervals[1:]:
            if  interval.start < heap[0][0]:
                heapq.heappush(heap, (interval.end, interval.start))
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, (interval.end, interval.start))
            minRooms = max(minRooms, len(heap))
        return minRooms

                