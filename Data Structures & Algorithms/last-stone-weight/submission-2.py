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

        















        # heap = [-1 *stone for stone in stones]
        # heapq.heapify(heap)

        # while len(heap)>1:
        #     print(heap)
        #     stone1 = heapq.heappop(heap)
        #     stone2 = heapq.heappop(heap)
        #     dif = max(stone1,stone2) - min(stone1,stone2)

        #     if dif>0 : 
        #         heapq.heappush(heap, dif)

        # if len(heap) == 1:
        #     return heap[0]
        # else:
        #     return 0
            
        