# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val: 
                return False
            return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

        if not subRoot:
            return True
        if not root: 
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)















   
        
    #     if not root and not subRoot:
    #         return True
    #     elif not root:
    #         return False
    #     elif not subRoot:
    #         return True
    #     elif self.sameTree(root, subRoot):
    #         return True
    #     else:
    #         return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    # def sameTree(self, p,q):
    #     if not p and not q:
    #         return True
    #     elif not p or not q:
    #         return False
    #     elif p.val == q.val:
    #         return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)
    #     else:
    #         return False


        
        