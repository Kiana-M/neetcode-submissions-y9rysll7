class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        max_heap = [-1*i for i in nums]
        heapq.heapify(max_heap)
        for i in range(k):
            k_largest = heapq.heappop(max_heap)
        return -1*k_largest
        