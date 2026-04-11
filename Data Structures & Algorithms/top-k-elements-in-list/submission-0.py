class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1

        
        most_freq_list = sorted(count.values())[len(count.values())-k:len(count.values())]
        result = [element for element in count.keys() if count[element] in most_freq_list]

        return result
        