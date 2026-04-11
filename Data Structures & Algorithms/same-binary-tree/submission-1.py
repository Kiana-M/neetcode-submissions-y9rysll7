# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        if p.right and q.right:
            right_check = self.isSameTree(p.right, q.right)
        elif p.right or q.right:
            right_check = False
        else:
            right_check = True
        if p.left and q.left:
            left_check = self.isSameTree(p.left, q.left)
        elif p.left or q.left:
            left_check = False
        else:
            left_check = True

        return right_check and left_check
        