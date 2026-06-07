class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]]+1 if nums[i] in count else 1

        for num in count:
            freq[count[num]].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            if freq[i] == []:
                continue
            res.extend(freq[i])
            if len(res) >= k:
                return res[:k]
        return res