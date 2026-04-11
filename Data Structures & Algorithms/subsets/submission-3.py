class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i> len(nums)-1: #when to halt and return
                result.append(subset.copy())
                return result
            else:
                subset.append(nums[i])#like traversing to root.left
                dfs(i+1) 
                subset.pop()#like traversing to root.right
                dfs(i+1) 
        dfs(0)
        return result


            

























#         result = []
#         subset = []
#         def dfs(i):
#             if i > len(nums)-1:
#                 result.append(subset.copy())
#                 return result
#             subset.append(nums[i])
#             dfs(i+1)
#             subset.pop()
#             dfs(i+1)
#         dfs(0)
#         return result
        
'''
        
            1 /                  \ []
            [1]                  []
        2 /     \[]           2/    \[]
        [1,2]     [1]        [2]      []
        3/\[]      3/\[]     3/\[]    3/\[] 
 [1,2,3] [1,2] [1,3] [1]   [2,3] [2] [3] []
'''  