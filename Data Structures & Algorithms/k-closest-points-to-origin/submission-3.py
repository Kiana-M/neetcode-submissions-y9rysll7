class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, [dist, point])
        
        kclosest = []
        for i in range(k):
            closest = heapq.heappop(heap)
            kclosest.append(closest[1])
        return kclosest

        