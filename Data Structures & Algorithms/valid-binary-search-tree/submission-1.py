# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        sol = Solution()
        if not sol.isValidBST(root.left) or not sol.isValidBST(root.right):
            print(root)
            print("left right not valid")
            return False
        if root.left != None and root.val <= sol.getMaximum(root.left):
            print("root bigger than left max")
            return False
        if root.right != None and root.val >= sol.getMinimum(root.right):
            print("root smaller than right min")
            return False
        return True

    def getMaximum(self, root: TreeNode) -> int:
        while root.right != None:
            root = root.right
        return root.val
    
    def getMinimum(self, root: TreeNode) -> int:
        while root.left != None:
            root = root.left
        return root.val