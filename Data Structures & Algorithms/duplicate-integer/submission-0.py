class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for val in nums:
            if val in count_dict:
                return True
            else:
                count_dict[val] = 1
        return False
         