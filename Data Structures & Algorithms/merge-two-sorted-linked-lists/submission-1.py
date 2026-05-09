# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        mergedTail = dummy # so it can be a pointer to where to add the merged item in linkedlist

        while list1 and list2:
            if list1.val < list2.val:
                mergedTail.next = list1
                list1 = list1.next
            else:
                mergedTail.next = list2
                list2 = list2.next

            mergedTail = mergedTail.next
        
        if list1:
            mergedTail.next = list1
        elif list2:
            mergedTail.next = list2
        
        return dummy.next
