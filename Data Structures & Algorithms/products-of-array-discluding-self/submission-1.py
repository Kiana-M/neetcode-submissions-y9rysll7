class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums)+1)]
        #prefix multiplication:
        temp = 1
        for i in range(1,len(nums)):
            temp *= nums[i-1]
            output[i] = temp
        print(output)
        #postfix
        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp *= nums[i+1]
            output[i] *= temp

        return output[0:len(nums)]
    
            #nums=[1,2,4,6]
            #pre = [1,1,2,8]
            #post =[48,24,6,1]
            # out = [48, 24, 12,8]
            