class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #assuming there is no zero value:
        output = [0 for i in range(len(nums))]
        prod = 1
        zero_index = []
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zero_index.append(i)
                if len(zero_index) > 1:
                    return output
        
        
        output = [0 for i in range(len(nums))]
        if len(zero_index) == 1:
            output[zero_index[0]] = prod
            return output

        for i in range(len(nums)):
                output[i] = prod//nums[i]
        return output