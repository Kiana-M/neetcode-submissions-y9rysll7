class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        ct = 0

        for start, end in intervals[1:]:
            if start < prevEnd: #overlap
                ct += 1
                prevEnd = min(end,prevEnd)
            else:
                prevEnd = end

        return ct