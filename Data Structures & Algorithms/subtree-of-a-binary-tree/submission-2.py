# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        elif not root:
            return False
        elif not subRoot:
            return True
        elif self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def sameTree(self, p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)
        else:
            return False


        
        