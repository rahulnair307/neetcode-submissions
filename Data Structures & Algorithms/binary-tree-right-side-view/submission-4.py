# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # okay so for each level we want the right most node - use BFS - level order traversal
        if not root:
            return []
        
        res = []
        queue = collections.deque([root])

        while queue:
            rightSide = None
            levelSize = len(queue)

            for i in range(levelSize):
                node = queue.popleft()

                rightSide = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        return res
