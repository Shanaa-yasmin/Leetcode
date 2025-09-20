# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        # Count left and right recursively
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        # Total nodes = 1 (root) + left + right
        return 1 + left_count + right_count

        

        
