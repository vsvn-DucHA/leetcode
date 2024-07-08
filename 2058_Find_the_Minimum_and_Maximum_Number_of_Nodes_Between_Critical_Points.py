# Definition for singly-linked list.
import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"


# class Solution:
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         min_index = math.inf
#         min_distance = math.inf
#         last_critical_point_index = 0
#         critical_point_qty = 0
#         index = 0
#         pre_node = None

#         def check_next_node(node: ListNode, pre_node: ListNode):
#             if not (node.next and pre_node):
#                 return False
#             if (node.val - pre_node.val) * (node.val - node.next.val) > 0:
#                 return True
#             return False

#         while head:
#             if check_next_node(head, pre_node):
#                 critical_point_qty += 1
#                 # print(
#                 #     "-",
#                 #     index,
#                 #     ", min_distance:",
#                 #     min_distance,
#                 #     ", min_index:",
#                 #     min_index,
#                 # )
#                 min_index = min(min_index, index)
#                 if critical_point_qty >= 2:
#                     min_distance = min(min_distance, index - last_critical_point_index)
#                 last_critical_point_index = index
#                 # print(
#                 #     "+",
#                 #     index,
#                 #     ", min_distance:",
#                 #     min_distance,
#                 #     ", min_index:",
#                 #     min_index,
#                 # )
#             pre_node = head
#             index += 1
#             head = head.next

#         return (
#             [min_distance, last_critical_point_index - min_index]
#             if critical_point_qty >= 2
#             else [-1, -1]
#         )


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indexs: list[int] = []
        pre_node = None
        index = 0

        def check_next_node(node: ListNode, pre_node: ListNode):
            if not (node.next and pre_node):
                return False
            if (node.val - pre_node.val) * (node.val - node.next.val) > 0:
                return True
            return False

        while head:
            if check_next_node(head, pre_node):
                indexs.append(index)

            pre_node = head
            index += 1
            head = head.next
        length = len(indexs)
        if length < 2:
            return [-1, -1]
        min_instance = 1e5 + 1
        for i in range(1, length):
            if min_instance > indexs[i] - indexs[i - 1]:
                min_instance = indexs[i] - indexs[i - 1]
        return [min_instance, indexs[length - 1] - indexs[0]]


arr = [5, 3, 1, 2, 5, 1, 2]
node = head = ListNode(val=arr[0])

for i in range(len(arr)):
    if i == 0:
        continue
    new_node = ListNode(val=arr[i])
    node.next = new_node
    node = new_node


s = Solution()
print(s.nodesBetweenCriticalPoints(head))
