class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1000
        r, l = 0, len(nums)-1

        while r <= l:
            # if nums[l] < nums[r]:
            #     res = min(res,nums[l])
            #     break

            mid = (l+r)//2
            res = min(res, nums[mid]) 
            if nums[mid] >= nums[l]:
                # we are at the right sorted portion,
                # so need to move farther right
                r = mid + 1
            else:
                # we are at the left sorted portion,
                # so need to stay here 
                l = mid - 1
        return min(res, nums[0])
        
                
        #r, l , mid = 0, 6, 3
        #r, l, mid = 0, 4, 2
        #r, l , mid = 3, 3, 3