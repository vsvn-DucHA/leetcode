# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next:'ListNode'=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f'val: {self.val}, next:[{self.next}]'
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node=head
        n=0
        while node:
           n+=1
           node=node.next 
        first_n_th=n%k
        nums_of_parts=n//k
        node,res=head,[]
        print(first_n_th,nums_of_parts)
        while len(res)<first_n_th:
            res.append(node)
            for _ in range(nums_of_parts):
                node=node.next
            prenode=node
            node=node.next
            prenode.next=None
        while len(res)<k and node:
            res.append(node)
            for _ in range(nums_of_parts-1):
                node=node.next
            prenode=node
            node=node.next
            prenode.next=None
        while len(res)<k:
            res.append(None)
        return res
    
arr=[1,2,3,4,5,6,7,8,9,10]
k=3
head=node=ListNode()
for i in arr:
    node.next=ListNode(i)
    node=node.next
s= Solution()
res=(s.splitListToParts(head.next,k))
for i in res:
    print(i)
print(len(res))