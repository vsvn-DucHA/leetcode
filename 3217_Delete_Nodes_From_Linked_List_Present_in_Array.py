# Definition for singly-linked list.
import time
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        virtual_node = ListNode(next=head)
        nums = set(nums)
        head = virtual_node
        while head:
            # print(head.val)
            while head.next and head.next.val in nums:
                head.next = head.next.next
            head = head.next
        return virtual_node.next


nums = list(range(0, 100000))
head = [50004] * 100000
h = node = ListNode(0, None)
for i in head:
    new_node = ListNode(i, None)
    node.next = new_node
    node = new_node
h = h.next

s = Solution()
t1 = time.time()
m = s.modifiedList(nums, h)
t2 = time.time()
print(t2 - t1)
# while m:
#     print(m.val)
#     m = m.next
