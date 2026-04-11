class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1* stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            heaviest = heapq.heappop(stones) 
            heavier = heapq.heappop(stones)
            if heavier != heaviest:
                heapq.heappush(stones, heaviest-heavier)
        if len(stones) == 1:
            return stones[0]*(-1)
        elif len(stones) ==0:
            return 0 
