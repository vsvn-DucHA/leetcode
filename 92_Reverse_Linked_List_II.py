# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next:'ListNode'=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f'val: {self.val}, next: [{self.next}]'
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right: return head
        node=head=ListNode(0,head)
        i=0
        # i<left-1 và duyệt
        while i<left-1:
            node=node.next
            i+=1
        #i = left-1 lưu lại node trước left 
        preNode=node
        node=node.next
        i+=1
        # left < i =<right bắt đầu reverse
        # đổi theo thứ tự a b c d -> a c b d -> a d c b (đảo node ra sau preNode)
        while i<right:
            reversedNode=node.next
            node.next=node.next.next
            reversedNode.next=preNode.next
            preNode.next=reversedNode
            i+=1 
        return head.next
    
arr=[1,2,3,4,5,6,7,8,9,10]
head=node=ListNode()
for i in arr:
    node.next=ListNode(i)
    node=node.next
    
left=2
right=4
s=Solution()
print(s.reverseBetween(head.next,left,right))
