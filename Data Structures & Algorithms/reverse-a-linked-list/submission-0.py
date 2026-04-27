# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### Iterative Approach

        prev = None
        curr = head

        while curr: # traverse through the linked list until the end
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev # at the end this is the new head

        # ### Recursive Approach

        # if head is None or head.next is None:
        #     return head
        
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p