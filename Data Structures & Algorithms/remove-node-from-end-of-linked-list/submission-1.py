# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        node=head
        N=0
        while node:
            N+=1
            node=node.next
        if N==1:
            return None
        node=dummy
        for i in range(N-n):
            node=node.next
        if node.next:
            node.next=node.next.next
        else:
            node.next=None
        return dummy.next



        

        