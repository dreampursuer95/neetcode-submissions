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
        if root.left != None:
            isValid, minVal, maxVal = sol.isValidBSTWithMinMax(root.left)
            if not isValid:
                return False
            if root.val <= maxVal:
                return False
        if root.right != None:
            isValid, minVal, maxVal = sol.isValidBSTWithMinMax(root.right)
            if not isValid:
                return False
            if root.val >= minVal:
                return False
        return True
    
    def isValidBSTWithMinMax(self, curr: Optional[TreeNode]) -> tuple[bool, int, int]:
        sol = Solution()
        minValReturned = maxValReturned = curr.val
        if curr.left != None:
            isValid, minVal, maxVal = sol.isValidBSTWithMinMax(curr.left)
            if not isValid:
                return False, 0, 0
            if curr.val <= maxVal:
                return False, 0, 0
            minValReturned = min(minVal, curr.left.val)
        if curr.right != None:
            isValid, minVal, maxVal = sol.isValidBSTWithMinMax(curr.right)
            if not isValid:
                return False, 0, 0
            if curr.val >= minVal:
                return False, 0, 0
            maxValReturned = max(maxVal, curr.right.val)
        return True, minValReturned, maxValReturned
