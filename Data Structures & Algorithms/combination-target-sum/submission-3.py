class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #not efficient
        result = []
        def backtrack(j, path):
            if sum(path)==target:
                result.append(path.copy())
                return

            for i in range(j, len(nums)):
                if sum(path)>target:
                    break
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0,[])
        return result
        