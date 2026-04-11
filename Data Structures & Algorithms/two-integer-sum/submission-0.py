class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in ind_dict:
                return [ind_dict[target - nums[i]], i]
            else:
                ind_dict[nums[i]] = i
        


        