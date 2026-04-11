class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            if i>len(nums)-1:
                res.append(subset.copy())
                return res
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i +=1
            dfs(i+1)
        dfs(0)
        #res = list(set(res))
        return res
        