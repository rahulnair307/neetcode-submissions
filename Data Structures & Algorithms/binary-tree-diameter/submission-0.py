# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]

        def getEdges(root):
            if not root:
                return 0
            
            leftEdges = getEdges(root.left)
            rightEdges = getEdges(root.right)
            currDiameter = leftEdges + rightEdges

            maxDiameter[0] = max(maxDiameter[0], currDiameter)
            return 1 + max(leftEdges, rightEdges)
            
        getEdges(root)
        return maxDiameter[0]    # sets a paticular memory spot and sets local variable equal to that so need to make to list
