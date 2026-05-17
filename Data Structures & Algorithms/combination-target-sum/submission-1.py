class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(j, path):
            if sum(path) == target:
                result.append(path.copy())
                return

            for i in range(j, len(nums)):
                if nums[i] + sum(path) > target:
                    break

                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])
        return result

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # res = []
        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return res
        #     if i>=len(nums) or total>target:
        #         return
        #     cur.append(nums[i])
        #     dfs(i, cur, total+nums[i])#?
        #     cur.pop()
        #     dfs(i+1, cur, total)

        # dfs(0,[], 0)
        # return res
        