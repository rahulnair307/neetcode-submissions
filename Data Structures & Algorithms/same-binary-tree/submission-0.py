# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False

        # queueP = deque([p])
        # queueQ = deque([q])

        # while queueP and queueQ:
        #     nodeP = queueP.popleft()
        #     nodeQ = queueQ.popleft()

        #     # values must match
        #     if nodeP.val != nodeQ.val:
        #         return False

        #     # check left children
        #     if (nodeP.left and not nodeQ.left) or (not nodeP.left and nodeQ.left):
        #         return False
        #     if nodeP.left and nodeQ.left:
        #         queueP.append(nodeP.left)
        #         queueQ.append(nodeQ.left)

        #     # check right children
        #     if (nodeP.right and not nodeQ.right) or (not nodeP.right and nodeQ.right):
        #         return False
        #     if nodeP.right and nodeQ.right:
        #         queueP.append(nodeP.right)
        #         queueQ.append(nodeQ.right)

        # # if both queues are empty, trees are the same
        # return not queueP and not queueQ