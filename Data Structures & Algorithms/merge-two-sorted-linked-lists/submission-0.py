# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        res=dummy
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy1=list1
        dummy2=list2
        while dummy1 and dummy2:
            if dummy1.val<dummy2.val:
                res.next=dummy1
                dummy1=dummy1.next
            else:
                res.next=dummy2
                dummy2=dummy2.next
            
            res=res.next
        while dummy1:
            res.next=dummy1
            
            res=res.next
            dummy1=dummy1.next
        while dummy2:
            res.next=dummy2
            
            res=res.next
            dummy2=dummy2.next

        return dummy.next


        