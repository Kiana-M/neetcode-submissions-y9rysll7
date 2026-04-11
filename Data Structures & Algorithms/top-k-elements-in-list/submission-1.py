class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # have a list where index is repetition and element is a list of ints that have that repetition
        freq = [[] for i in range(len(nums)+1)]
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        print(counts)
        for key, value in counts.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq)-1, -1, -1):
            print(freq[i])
            if freq[i] == []:
                continue
            else:
                res.extend(freq[i])
                if len(res)>=k:
                    return res[0:k]




