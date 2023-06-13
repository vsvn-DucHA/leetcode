from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node = self
        res = []
        while node.next:
            res.append(node.val)
            node = node.next
        return str(res)
        # return node.val


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = headBlock = headBlock_check = head
        checkNumberNode = True
        for i in range(k-1):
            if headBlock_check.next:
                headBlock_check = headBlock_check.next
            else:
                checkNumberNode = False
        while head != headBlock_check and checkNumberNode:
            nextNode = node.next
            node.next = nextNode.next
            nextNode.next = head
            head = nextNode
        while node.next:
            checkNumberNode = True
            endPreviousBlock = node
            headBlock = headBlock_check = node = node.next

            for i in range(k-1):
                if headBlock_check.next:
                    headBlock_check = headBlock_check.next
                else:
                    checkNumberNode = False
            while headBlock != headBlock_check and checkNumberNode:

                nextNode = node.next
                node.next = nextNode.next
                nextNode.next = headBlock
                headBlock = nextNode
                endPreviousBlock.next = headBlock

        return head


nums = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
head = node = ListNode()
for i in nums:
    node.val = i
    nextNode = ListNode()
    node.next = nextNode
    node = node.next
print(head)
print(s.reverseKGroup(head, 3))
