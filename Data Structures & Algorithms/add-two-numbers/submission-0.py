# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=""
        num2=""
        node1=l1
        node2=l2
        while node1:
            num1+=str(node1.val)
            node1=node1.next
        while node2:
            num2+=str(node2.val)
            node2=node2.next
        num1=num1[::-1]
        num2=num2[::-1]
        num=int(num1)+int(num2)
        num=str(num)
        num=num[::-1]
        res=ListNode(num[0])
        dummy=ListNode(0,res)
        for i in range(1,len(num)):
            res.next=ListNode(num[i])
            res=res.next       
        return dummy.next