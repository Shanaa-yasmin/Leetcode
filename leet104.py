# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        # Base case: if tree is empty
        if not root:
            return 0
        
        # Recursive case: compute left and right depths
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Current depth = 1 (for root) + max of children depths
        return 1 + max(left_depth, right_depth)
