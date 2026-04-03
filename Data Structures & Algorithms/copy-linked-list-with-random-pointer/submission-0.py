"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node=head
        dico={None:None}
        while node:
            node_c=Node(node.val)
            dico[node]=node_c
            node=node.next
        node=head
        while node: 
            node_c=dico[node]
            node_c.next=dico[node.next]
            node_c.random=dico[node.random]
            node=node.next
        return dico[head]


        