class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        
        while len(intervals)>1:
            while intervals[0][1] >= intervals[1][0]:
                #overlap
                newInterval = [intervals[0][0], max(intervals[0][1], intervals[1][1])]
                intervals.pop(0)
                intervals.pop(0)
                intervals.append(newInterval)
                intervals.sort()
                if len(intervals)<2:
                    break
            res.append(intervals[0])
            print(res)
            intervals.pop(0)
        if intervals:
            res.append(intervals[0])
        return res
            



        