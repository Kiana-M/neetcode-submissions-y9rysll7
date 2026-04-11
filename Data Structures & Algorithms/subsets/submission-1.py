class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i > len(nums)-1:
                result.append(subset.copy())
                return result
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result
        
'''
        
            1 /                  \ []
            [1]                  []
        2 /     \[]           2/    \[]
        [1,2]     [1]        [2]      []
        3/\[]      3/\[]     3/\[]    3/\[] 
 [1,2,3] [1,2] [1,3] [1]   [2,3] [2] [3] []
'''  