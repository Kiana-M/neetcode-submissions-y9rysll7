class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(j,path):
            if sum(path) == target:
                res.append(path.copy())
            
            for i in range(j, len(nums)):
                if sum(path)>target:
                    continue
                path.append(nums[i])
                backtrack(i,path)
                path.pop()

        backtrack(0,[])
        return res

        