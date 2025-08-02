# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.left==root.right==None:
            return targetSum==root.val
        remsum=targetSum-root.val
        return (self.hasPathSum(root.left,remsum) or self.hasPathSum(root.right,remsum))


OR


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            if not node:
                return False

            currentSum += node.val

            if not node.left and not node.right:
                return currentSum == targetSum

            left = dfs(node.left, currentSum)
            right = dfs(node.right, currentSum)
            return left or right

        return dfs(root, 0) if root else False
