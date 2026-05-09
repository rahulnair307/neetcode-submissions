# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # binary tree left and right subtrees of every node differ in height by no more than 1
        # subproblem: 
        resultBoolean = [True]
        possibleValues = [0,1,-1]

        def getHeight(root):
            # basecase
            if not root:
                return 0
                
            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)
            if leftHeight - rightHeight not in possibleValues:
                resultBoolean[0] = False
            
            return 1 + max(leftHeight, rightHeight)
        
        getHeight(root)
        return resultBoolean[0]