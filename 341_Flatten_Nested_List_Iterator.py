# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import collections
from typing import List


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> ['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
class NestedIterator:
  def __init__(self, nestedList: List[NestedInteger]):
    # Initialize a deque to store the flattened integers
    self.q = collections.deque()
    # Call the addInteger function to add integers to the deque
    self.addInteger(nestedList)

  def next(self) -> int:
    # Remove and return the leftmost element from the deque
    return self.q.popleft()

  def hasNext(self) -> bool:
    # Return True if the deque is not empty, False otherwise
    return bool(self.q)

  def addInteger(self, nestedList: List[NestedInteger]) -> None:
    # Iterate over the elements in the nestedList
    for ni in nestedList:
      # If the element is an integer, add it to the deque
      if ni.isInteger():
        self.q.append(ni.getInteger())
      # If the element is a list, recursively call the addInteger function to add integers to the deque
      else:
        self.addInteger(ni.getList())