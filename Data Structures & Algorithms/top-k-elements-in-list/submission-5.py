class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            freq[count[num]].append(num)
        
        result = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i] != []:
                result.extend(freq[i])
            if len(result) >= k:
                return result[0:k]
        

        