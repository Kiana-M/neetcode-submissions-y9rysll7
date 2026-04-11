class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # a dictheap where each element is a dict of distance: [point1,point2]

        for pt in points:
            dist = math.sqrt(pt[0]**2 + pt[1]**2)
            heapq.heappush(heap, [dist, pt[0], pt[1]])
        print(heap)
        res = []
        for i in range(k):
            dist, ptx, pty = heapq.heappop(heap)
            res.append([ptx, pty])
        return res
        