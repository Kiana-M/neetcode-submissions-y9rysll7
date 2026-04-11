class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                #overlap
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res
        
        # res = []
        # intervals = sorted(intervals)
        
        # while len(intervals)>1:
        #     while intervals[0][1] >= intervals[1][0]:
        #         #overlap
        #         newInterval = [intervals[0][0], max(intervals[0][1], intervals[1][1])]
        #         intervals.pop(0)
        #         intervals.pop(0)
        #         intervals.append(newInterval)
        #         intervals.sort()
        #         if len(intervals)<2:
        #             break
        #     res.append(intervals[0])
        #     print(res)
        #     intervals.pop(0)
        # if intervals:
        #     res.append(intervals[0])
        # return res
            



        