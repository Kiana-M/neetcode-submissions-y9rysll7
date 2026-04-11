"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        overlapping_ends_heap = []
        
        for interval in intervals:
            if overlapping_ends_heap and overlapping_ends_heap[0] <= interval.start:
                heapq.heappop(overlapping_ends_heap)
            heapq.heappush(overlapping_ends_heap, interval.end)
    
        return len(overlapping_ends_heap)
        