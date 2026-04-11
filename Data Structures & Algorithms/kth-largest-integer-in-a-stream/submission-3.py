class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]























    #     #create a min heap of size k with k largest elements of the list
    #     self.k = k
    #     self.minheap = nums
    #     heapq.heapify(self.minheap)
    #     while len(self.minheap) > self.k:
    #         heapq.heappop(self.minheap)

        

    # def add(self, val: int) -> int:
       