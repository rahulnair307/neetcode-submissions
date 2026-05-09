# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # this while loop has the right pointer n spaces 
        while n > 0 and right:
            right = right.next
            n -= 1
        # moves right to the end and left to the nth index from end - 1
        while right:
            left = left.next
            right = right.next
        
        #position the pointer to "remove" nth element
        left.next = left.next.next
        # return the proper head that is why we keep dummy so it can return in this edge case
        return dummy.next