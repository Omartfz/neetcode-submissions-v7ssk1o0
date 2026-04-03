# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen={}
        dummy=ListNode()
        dummy.next=head
        node=dummy.next
        index=0
        while node:
            if node in seen:
                return True
            else:
                seen[node]=index
            index+=1
            node=node.next
        return False


            

        