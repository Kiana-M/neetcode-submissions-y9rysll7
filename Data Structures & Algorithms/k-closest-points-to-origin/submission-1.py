class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #hash map of point to distance from origin:
        distance = {}
        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            if dist in distance:
                distance[dist].append(p)
            else:
                distance[dist] = [p]
        
        lengths = list(distance.keys())
        lengths.sort()

        res = []
        for i in range(k):
            res.extend(distance[lengths[i]])
            if len(res)>=k:
                return res
        
            
        