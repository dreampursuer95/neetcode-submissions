# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(curr, minVal, maxVal):
            if curr == None:
                return True
            if not minVal < curr.val < maxVal:
                return False
            return is_valid(curr.left, minVal, curr.val) and is_valid(curr.right, curr.val, maxVal)
        return is_valid(root, float('-inf'), float('inf'))
