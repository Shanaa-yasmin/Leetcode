# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def preorder(node):
            if not node:
                return
            preorder(node.left)
            result.append(node.val)
            preorder(node.right)
        preorder(root)
        return result
