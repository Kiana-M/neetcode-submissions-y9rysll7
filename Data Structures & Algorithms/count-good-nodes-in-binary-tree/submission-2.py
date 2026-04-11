# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #sol 3 is better
    def goodNodes(self, root: TreeNode) -> int:
        good_num = 0
        if not root:
            return 0
        max_val_in_this_path = root.val

        def dfs(node, max_val):
            nonlocal good_num
            if not node:
                return 0
            if node.val >= max_val:
                good_num += 1
            max_val = max(node.val, max_val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, max_val_in_this_path)
        return good_num
        
        
            
        