# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num=""
        node1=l1
        node2=l2
        carry=0
        dummy=ListNode()
        node=dummy
        while node1 or node2 or carry:
            num1=node1.val if node1 else 0
            num2=node2.val if node2 else 0
            num=num1+num2+carry
            carry=num//10
            num=num%10
            node.next=ListNode(num)
            node=node.next
            node1=node1.next if node1 else None
            node2=node2.next if node2 else None
        return dummy.next
        