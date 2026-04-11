class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        ct = 0

        for start, end in intervals[1:]:
            if start < prevEnd: #overlap
                ct += 1
            else:
                prevEnd = end

        return ct