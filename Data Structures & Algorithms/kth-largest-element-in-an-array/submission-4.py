class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #in case of median, k = n//2
        k = len(nums) - k
        def quickselect(l, r):
            pivot = r-1
            partition = l

            for i in range(l, r):
                if nums[i] < nums[pivot]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    partition += 1
            nums[partition], nums[pivot] = nums[pivot], nums[partition]

            if k == partition:
                return nums[partition]
            if k > partition:
                return quickselect(partition+1, r)
            if k < partition:
                return quickselect(l, partition)
        return quickselect(0, len(nums))


        
