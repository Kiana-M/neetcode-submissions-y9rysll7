# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #use a hash set for p and a stack for q, when you get to q, start popping
        p_set = []
        q_stack = []
        def searchBST(node, a, lst):
            if a.val > node.val:
                lst.append(node)
                searchBST(node.right, a, lst)
            elif a.val < node.val:
                lst.append(node)
                searchBST(node.left, a, lst)
            else:
                lst.append(node)
                return node
        searchBST(root, p, p_set)
        searchBST(root, q, q_stack)

        while q_stack:
            cur = q_stack.pop()
            if cur in p_set:
                return cur
        return None

        
        