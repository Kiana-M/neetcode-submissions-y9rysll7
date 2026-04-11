# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #start from root, if p<node<q or q<nod<p: return
        #if node > p & q : turn left, else: turn right
        if root.val > p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif root.val < p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root
        