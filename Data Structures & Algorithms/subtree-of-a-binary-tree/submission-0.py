# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subtree of a binary tree remember all of this node's descendants
        
        def sameTree(p, q):
            if not p and not q:
                return True
                
            if (not p and q) or (not q and p):
                return False    # shape is not the same
            
            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        #another dfs function
        def hasSubTree(root):
            #clearly we have not found one here
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True
            
            return hasSubTree(root.left) or hasSubTree(root.right)
        
        return hasSubTree(root)

# Time: O(m*n) -> most optimal O(m+n)
# Space: O(n) -> 