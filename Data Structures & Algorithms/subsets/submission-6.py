class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #binary template
        # def backtrack(i, path):
        #     if i == len(nums):              # base: decided about every element
        #         result.append(path.copy())
        #         return
            
        #     # Choice 1: include nums[i]
        #     path.append(nums[i])
        #     backtrack(i + 1, path)
        #     path.pop()
            
        #     # Choice 2: exclude nums[i]
        #     backtrack(i + 1, path)
        result = []
        def backtrack(i, path):
            if i == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
            backtrack(i+1, path)
        backtrack(0,[])
        return result