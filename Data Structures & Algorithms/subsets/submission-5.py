class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # template:
        # def backtrack(path, choices):
        #     if goal_reached(path):
        #         results.append(path.copy())   # copy! path keeps mutating
        #         return
            
        #     for choice in choices:
        #         if not valid(choice, path):
        #             continue                  # prune
                
        #         path.append(choice)           # 1. make the choice
        #         backtrack(path, next_choices) # 2. recurse
        #         path.pop()                    # 3. UNDO ← the "backtrack"
        result = []
        def backtrack(j, path):
            result.append(path.copy())

            for i in range(j, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0,[])
        return result