"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x : x.start)
        end_times = [intervals[0].end]
        rooms = 1

        for i in range(1, len(intervals)):
            if end_times[0] > intervals[i].start:
                rooms += 1
            else:
                heapq.heappop(end_times)
            heapq.heappush(end_times, intervals[i].end)

        return rooms
            
