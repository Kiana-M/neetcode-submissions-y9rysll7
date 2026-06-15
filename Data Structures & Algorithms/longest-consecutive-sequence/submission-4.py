class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # note that this solution is not optimal compared to sol 1, 
        #u can paste in LC and look at examples, you'll see the difference
        numset = set(nums)
        longest = 0
        length = 0
        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                length = 1
                while nums[i]+length in numset:
                    length += 1
            longest = max(length, longest)
        return longest

        