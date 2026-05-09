# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = height_left + height_right
        largestDiameter = [0]
        def getHeight(root):
            if root is None:
                return 0
            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)
            currDiameter = leftHeight + rightHeight

            largestDiameter[0] = max(largestDiameter[0], currDiameter)
            
            return 1 + max(leftHeight,rightHeight)

        getHeight(root)
        return largestDiameter[0]
    
    #Time = O(n)
    #space = O(h)