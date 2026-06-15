class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        distance = []
        for p in points:
            euc_dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(distance, [euc_dist, p[0], p[1]])
        
        res = []
        for i in range(k):
            dist, px, py = heapq.heappop(distance)
            res.append([px,py])
        
        return res
            
            