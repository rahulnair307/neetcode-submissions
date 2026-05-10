# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # nodes are unique
        # binary search tree so the left subtree all nodes smaller than node.val and right greater than node.val
        # ancestor is going up tree and descendant is going down the tree
        lca = [root] # putting in list to make a proper global variable

        def search(root):
            if not root:
                return

            lca[0] = root

            if root.val == p.val or root.val == q.val:
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:   # roots value is between them not going to find a better ancestor than curr
                return
        
        search(root)
        return lca[0]