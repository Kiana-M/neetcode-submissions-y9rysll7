class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j<k:
                add = nums[i] + nums[j] + nums[k]
                if add < 0:
                    j += 1
                elif add > 0:
                    k -= 1
                else:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        
        return res