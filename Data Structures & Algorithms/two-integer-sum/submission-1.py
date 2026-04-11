class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}

        for i in range(len(nums)):
            #check if target-value is in hash
            if target - nums[i] in elements:
                return [elements[target - nums[i]], i]
            # ow, add it to hash
            else:
                elements[nums[i]] = i

        